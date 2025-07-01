# Makefile
#

prefix = /usr/local
exec_prefix = $(prefix)
bindir = $(exec_prefix)/bin
datarootdir = $(prefix)/share
datadir = $(datarootdir)
mandir = $(datarootdir)/man
man1dir = $(mandir)/man1
version = 3.8.9b
distdir = shc-$(version)
distfile = $(distdir).tgz

# For SCO
CFLAGS = -b elf -O -D_SVID

# For IRIX
CFLAGS = -xansi -fullwarn -O3 -g0

# For Solaris
CFLAGS = -fast -xO4 -s -v -Xa

# For HPUX
CFLAGS = -Wall -O -Ae

# For OSF1
CFLAGS = -w -verbose -fast -std1 -g0

# For GNU C compiler
CFLAGS = -Wall # -O6 -pedantic

#SHELL = /bin/sh

SHCFLAGS = -v -T # Add -T option to allow binary to be traceable

all: shc ask_for_test

shc: shc.c
	$(CC) $(CFLAGS) $@.c -o $@

ask_for_test:
	@echo '***	¿Do you want to probe shc with a test script?'
	@echo '***	Please try...	make test'

test: make_the_test ask_for_strings

make_the_test: match.x
	@echo '***	Running a compiled test script!'
	@echo '***	It must show files with substring "sh" in your PATH...'
	./match.x sh

match.x: shc match
	@echo '***	Compiling script "match"'
	CFLAGS="$(CFLAGS)" ./shc $(SHCFLAGS) -f match

ask_for_strings:
	@echo '***	¿Do you want to see strings in the generated binary?'
	@echo '***	Please try...	make strings'

strings: make_the_strings ask_for_expiration

make_the_strings: match.x
	@echo '***	Running: "strings -n 5 'match.x'"'
	@echo '***	It must show no sensible information...'
	strings -n 5 match.x

ask_for_expiration:
	@echo '***	¿Do you want to probe expiration date?'
	@echo '***	Please try...	make expiration'

expiration: til_yesterday ask_for_install

til_yesterday: shc match
	@echo '***	Compiling "match" to expired date'
	CFLAGS="$(CFLAGS)" ./shc $(SHCFLAGS) -vv -e `date "+%d/%m/%Y"` -f match
	@echo '***	Running a compiled test script!'
	@echo '***	It must fail showing "./match.x: has expired!"'
	./match.x || true

ask_for_install:
	@echo '***	¿Do you want to install shc?'
	@echo '***	Please try...	make install'

install: shc
	@echo '***	Installing shc and shc.1 on '$(DESTDIR)$(prefix)
	mkdir -p $(DESTDIR)$(bindir)
	install -c -s shc $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(man1dir)
	install -c -m 644 shc.1 $(DESTDIR)$(man1dir)
	gzip -fv $(DESTDIR)$(man1dir)/shc.1

clean:
	rm -f *.o *~ *.x.c

cleanall: clean
	rm -f shc *.x

clean-all: cleanall dist-clean

$(distdir):
	mkdir -p $(distdir)
	for i in CHANGES Copying LICENSE README.md makefile makefile.patch match pru.sh shc-3.8.9b.c shc.1 shc.README shc.c shc.html shc.md shc.spec test.bash test.csh test.ksh testit ; do cp $$i $(distdir); done

$(distfile):
	tar -cvzf $(distfile) $(distdir)

dist: $(distdir) $(distfile)

dist-clean:
	rm -rf $(distdir) $(distfile)
