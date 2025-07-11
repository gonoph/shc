%global debug_package %{nil}
%global forgeurl https://github.com/gonoph/shc

Name:		shc
Version:	3.8.9b
%forgemeta
Release:	1%{?dist}
Summary:	A generic shell script compiler.

License:	GPL
URL:		%{forgeurl}
Source0:	%{forgesource}

Requires:	gcc
BuildRequires:	gcc
BuildRequires:	make
# Requires:	

%description
A generic shell script compiler. Shc takes a script, which is specified on the
command line and produces C source code. The generated source code is then
compiled and linked to produce a stripped binary executable. Use with care.

%prep
%setup -q


%build
# make %{?_smp_mflags} CFLAGS="-Wall -O2 -Werror=implicit-function-declaration"
make CFLAGS="-Wall -O2 -Werror=implicit-function-declaration"


%install
%make_install DESTDIR=%{buildroot} prefix=/usr


%files
%attr(755, root, bin) /usr/bin/shc
%attr(644, root, bin) /usr/share/man/man1/shc.1.gz
%doc CHANGES Copying LICENSE README.md match pru.sh shc.README shc.html shc.md test.bash test.csh test.ksh testit


%changelog
* Mon Jun 30 2025 Billy Holmes <billy@gonoph.net> - 3.8.9b-1
- updates for spec file to build RPMs

* Fri Jan  4 2013 12:10:42 CET - 3.8.9b 
- Lee Chisnall <lee@dnuk.com>
- To work as daemon.  

* Wed Apr 25 2012 09:24:25 CEST - 3.8.9
- Thanks to Giacomo Picconi <giacomo.picconi@gpstudio.com> for:
- Fixing a long standing bug making the source not hidden.

* Mon Nov 28 2011 11:26:25 CEST - 3.8.8
- "me".

* Wed Feb 10 2010 20:40:37 CET - 3.8.7
- Bug on 64bit systems with expiration dates.

* Fri Jul  7 2006 15:54:39 CEST - 3.8.6
- Thanks to George Danchev <danchev@spnet.net> for:
- License clarification about the rc4 implementation.

* Fri Oct 21 2005 13:11:36 CEST - 3.8.5
- Thanks to Jukka A. Ukkonen <jau(a)iki.fi> for:
- Fixed untraceable() problems on FreeBSD.

* Tue Oct  4 2005 16:52:15 CEST - 3.8.4
- Thanks to Ron McOuat for:
- Fixed sma11 -d option bug.

* Tue Jun 28 2005 21:29:06 CEST - 3.8.3
- Thanks to Jacek Kalinski <jacek@dyski.one.pl> for:
- Fixed bug: "vfork" fails on multiprocessor systems.

* Thu Jun 16 2005 17:15:59 CEST - 3.8.2
- Thanks to Arjen Visser <arjen.visser@avisit.co.nz> for:
- Fixed bug: "rlax" used after encryption.
- Thanks to Nalneesh Gaur <Nalneesh.Gaur@accenture.com> for:
- Read permision of the script.x exposes it to disassembling.
- Group and others read permision is now removed by default.

* Thu Nov  4 2004 20:33:52 CET - 3.8
- Fixed incorrect implementation on rc4.
- Hidden all the binary executable symbols but one.
- Expiration date and most strings are encrypted too.
- All the encrypted payload is now randomized.

* Wed Jun 18 2003 16:32:26 CEST - 3.7
- Thanks to Philipp Koller <philipp@open.ch> for:
- Removed all strings in the compiled script.
- Improved program output and error messages.
- The -m option allows to define the *complete* expiration message.
- Updated manpage shc.1.
- Thanks to Bryan <bryan.hogan@dstintl.com> for:
- Fix wrong $0 on ksh.

* Fri Feb 21 2003 09:40:32 CET - 3.6
- Two new options:
  -D	switch on Debug exec calls.
  -T	switch off unTraceable.
- Bash does not need -- after -c.

* Mon Jan 20 2003 19:08:43 CET - 3.5
- Rewrite of large strings to silence the ISO C89 compiler warnings about
  strings larger than 509 characters.

* Tue Apr 16 2002 17:43:12 CEST - 3.4
- Remove "bad alignment" problem on AIX and other systems.
- Where exists, use /proc/<pid>/as in untraceable.

* Thu Jan 24 2002 21:27:07 CET - 3.3
- Prevent to ptrace the process.

* Tue Mar  9 1999 19:03:54 CET - 3.2
- Find ancient pclose that must be fclose.

* Tue Feb 16 1999 21:36:59 CET - 3.1
- Fixed a misbehavior on scripts with a in-frist-line option
	equal to "end of options" (i.e.  #!/bin/sh -- )
  (Thanks to Bernard Blundell <blundell@lts.sel.alcatel.de>)
- Stupid GCC "warning: return type of `main' is not `int'" removed.

* Tue Oct 14 1997 14:20:52 MET DST - 3.0
- Added a new option "-r" to force a relaxed security and
- so make a redistributable binary.
- Modified expiration day format. Now is dd/mm/yyyy.

* Fri Jun  6 1997 22:09:05 WET DST - 3.0b3
- Yet other few bugs fixed.
- Output format simplified.
- -pedantic compilation.

* Tue Jun  3 1997 17:51:51 GMT - 3.0b2
- Some explicit type conversions removed.
- Fixed the bug "END_OF_FILE" when compiling the generated code.
- A flush is needed before a pclose.
- st_blksize and st_blocks struct stat fields does not exist on SCO, both not
  used now.

* Wed Feb 26 1997 14:27:22 WET - 3.0b1
- The main difference with 2.4 is that in it the script was compressed an then
  shuffle around, now int 3.0 the script is encripted with an inline code, so
  not needend any external comand to work, and been faster at startup. Other
  related adventage is that the only information not encripted in .x.c is an
  stamp, expiration date and provider email address.
- Something equivalent to cheksums have been used to enforced at execution that
  the executing shell has not been modified from the time the script was
  compiled. If anybody tries to change the excuting shell, .x will refuse to
  execute.
- The generated .x.c source code is now readable.

