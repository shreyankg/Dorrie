ifndef LANGUAGES
LANGUAGES := $(shell grep -v "^\#" po/LINGUAS)
endif
PO_FILES = $(filter-out po/en.po,$(wildcard po/*.po))
MO_FILES = $(PO_FILES:.po=.mo)
HTML_FILES = $(shell find data -name "*.html")

PYTHON = python
PYBABEL = pybabel
BASEPATH = /
PWD = $(shell pwd)

all: $(LANGUAGES)
	cp static/robots.txt out/

$(LANGUAGES): % : po/%.mo data/templates/translations.html
	$(PYTHON) build/build.py -o out -i data/content -l $@ -p po -s static -b $(BASEPATH)

po/en.po: po/dorrie.pot
	cp po/dorrie.pot po/en.po

po/%.po: po/dorrie.pot
	msgmerge --no-wrap --update $@ $^
	@touch $@

po/en.mo: po/en.po
	msgfmt -o $@ $<

po/%.mo: po/%.po
	msgfmt -o $@ $<

po/dorrie.pot: $(HTML_FILES)
	${PYBABEL} extract -F build/pybabel.cfg data -o $@

data/templates/translations.html: po/LINGUAS
	$(PYTHON) build/translations.py $^ > $@

clean:
	rm -rf out
	rm -f po/en.po
	rm -f po/*.mo
	rm -f data/templates/translations.html
	rm -f build/rss.cache

msgmerge: $(wildcard po/*.po)

push:
	git push

httpd/conf/httpd.conf: httpd/conf/httpd.conf.in
	cp httpd/conf/httpd.conf.in httpd/conf/httpd.conf
	sed -i \
		-e 's#@SERVERROOT@#$(PWD)/httpd#g' \
		-e 's#@DOCUMENTROOT@#$(PWD)/out#g' \
		httpd/conf/httpd.conf

httpd/conf/languages.conf.in: po/LINGUAS
	$(PYTHON) build/buildconf.py $^ > $@

httpd/conf/languages.conf: httpd/conf/languages.conf.in
	cp httpd/conf/languages.conf.in httpd/conf/languages.conf
	sed -i \
		-e 's#@SERVERROOT@#$(PWD)/httpd#g' \
		-e 's#@DOCUMENTROOT@#$(PWD)/out#g' \
		httpd/conf/languages.conf

test: httpd/conf/httpd.conf httpd/conf/languages.conf
	/usr/sbin/httpd -d httpd -f conf/httpd.conf
	@echo "Test instance started at: http://localhost:5000/"

stoptest:
	pid=`cat httpd/run/httpd.pid` && \
	kill -TERM $$pid

.PHONY: all clean push test stoptest
