Summary:	Firmware for the Intel(R) PRO/Wireless 2100 Driver
Summary(pl):	Firmware dla sterownika do kart Intel(R) PRO/Wireless 2100
Name:		ipw2100-firmware
Version:	1.2
Release:	1
License:	distributable
Group:		System Environment/Kernel
Source0:	http://cache-www.intel.com/cd/00/00/09/63/96377_96377.zip
# Source0-md5:	817b987a89e811b87384968ffe15615f
URL:		http://ipw2100.sourceforge.net/firmware.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This package contains the firmware for the ipw-2100 driver. Usage of
the firmware is subject to the terms contained in
%{_defaultdocdir}/%{name}-%{version}/LICENSE*. Please read the license
carefully.

%description -l pl
Ten pakiet zawiera firmware dla sterownika ipw-2100. Mo¿na go u¿ywaæ
na warunkach zawartych w pliku
%{_defaultdocdir}/%{name}-%{version}/LICENSE*. Proszê uwa¿nie
przeczytaæ licencjê.

%prep
%setup -q -c
gunzip -c ipw2100-fw-%{version}.tgz | tar -xf -

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/firmware
install -d $RPM_BUILD_ROOT%{_libdir}/hotplug/firmware

install -p *.fw $RPM_BUILD_ROOT%{_sysconfdir}/firmware
cd $RPM_BUILD_ROOT%{_sysconfdir}/firmware
for file in *.fw; do
	ln -s %{_sysconfdir}/firmware/$file $RPM_BUILD_ROOT%{_libdir}/hotplug/firmware
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_sysconfdir}/firmware/*.fw
%{_libdir}/hotplug/firmware/*.fw
