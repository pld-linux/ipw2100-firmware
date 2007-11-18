Summary:	Firmware for the Intel(R) PRO/Wireless 2100 Driver
Summary(pl.UTF-8):	Firmware dla sterownika do kart Intel(R) PRO/Wireless 2100
Name:		ipw2100-firmware
Version:	1.3
Release:	2
License:	distributable
Group:		Base/Kernel
Source0:	http://bughost.org/firmware/ipw2100-fw-%{version}.tgz
# Source0-md5:	46aa75bcda1a00efa841f9707bbbd113
URL:		http://ipw2100.sourceforge.net/firmware.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the ipw-2100 driver. Usage of
the firmware is subject to the terms contained in
%{_docdir}/%{name}-%{version}/LICENSE*. Please read the license
carefully.

%description -l pl.UTF-8
Ten pakiet zawiera firmware dla sterownika ipw-2100. Można go używać
na warunkach zawartych w pliku
%{_docdir}/%{name}-%{version}/LICENSE*. Proszę uważnie
przeczytać licencję.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install -p *.fw $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
/lib/firmware/*.fw
