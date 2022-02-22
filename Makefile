#
# Global Settings
#
 
INSTALL = install
DESTDIR ?= /
PREFIX ?= $(DESTDIR)/usr
 
PATH_EXECUTABLE = $(PREFIX)/bin/
PATH_SOURCE_PY = /etc/capp_launcher/
 
#
# Targets
#
 
all:
	echo "/usr/bin/python /etc/capp_launcher/main.py" >> capp_launcher
 
install:
	$(INSTALL) -m0755 -D capp_launcher $(PATH_EXECUTABLE)/capp_launcher
	$(INSTALL) -d $(PATH_SOURCE_PY)
	$(INSTALL) -m0644 -D src/* $(PATH_SOURCE_PY)
 
uninstall:
	rm -rf $(PATH_EXECUTABLE)/capp_launcher
	rm -rf $(PATH_SOURCE_PY)
 
clean:
	rm -rf capp_launcher
