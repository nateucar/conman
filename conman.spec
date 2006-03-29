# $Id$

Name:		@PROJECT@
Version:	@VERSION@
Release:	1

Summary:	ConMan - The Console Manager
Group:		Applications/Communications
License:	GPL
URL:		http://www.llnl.gov/linux/conman/

BuildRoot:	%{_tmppath}/%{name}-%{version}

Source0:	%{name}-%{version}.tgz

%description
ConMan is a console management program designed to support a large
number of console devices and simultaneous users.  It currently supports
local serial devices and remote terminal servers (via the telnet protocol).
Its features include:

  - mapping symbolic names to console devices
  - logging all output from a console device to file
  - supporting monitor (R/O), interactive (R/W), and
    broadcast (W/O) modes of console access
  - allowing clients to join or steal console "write" privileges
  - executing Expect scripts across multiple consoles in parallel

%prep
%setup

%build
%configure
make

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"
DESTDIR="$RPM_BUILD_ROOT" make install

%clean
rm -rf "$RPM_BUILD_ROOT"

%pre
if [ -x /etc/rc.d/init.d/conman ]; then
  if /etc/rc.d/init.d/conman status | grep running >/dev/null 2>&1; then
    /etc/rc.d/init.d/conman stop
  fi
fi

%post
if [ -x /etc/rc.d/init.d/conman ]; then
  [ -x /sbin/chkconfig ] && /sbin/chkconfig --del conman
  [ -x /sbin/chkconfig ] && /sbin/chkconfig --add conman
  if ! /etc/rc.d/init.d/conman status | grep running >/dev/null 2>&1; then
    /etc/rc.d/init.d/conman start
  fi
fi

%preun
if [ "$1" = 0 ]; then
  if [ -x /etc/rc.d/init.d/conman ]; then
    [ -x /sbin/chkconfig ] && /sbin/chkconfig --del conman
    if /etc/rc.d/init.d/conman status | grep running >/dev/null 2>&1; then
      /etc/rc.d/init.d/conman stop
    fi
  fi
fi

%files
%defattr(-,root,root,0755)
%doc ChangeLog
%doc COPYING
%doc DISCLAIMER
%config(noreplace) /etc/conman.conf
%config(noreplace) /etc/logrotate.d/conman
/etc/rc.d/init.d/conman
%{_bindir}/conman
%{_bindir}/conmen
%{_sbindir}/conmand
%dir %{_libdir}/conman
%{_libdir}/conman/alpha.exp
%{_libdir}/conman/conman.exp
%dir %{_libdir}/conman/examples
%{_libdir}/conman/examples/boot_alpha.exp
%{_libdir}/conman/examples/mac.exp
%{_libdir}/conman/examples/rmc.exp
%{_libdir}/conman/examples/srm.exp
%{_libdir}/conman/examples/wtf.exp
%{_mandir}/man1/conman.1*
%{_mandir}/man5/conman.conf.5*
%{_mandir}/man8/conmand.8*