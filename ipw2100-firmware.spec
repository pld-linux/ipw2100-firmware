Summary:	Firmware for the Intel® PRO/Wireless 2100 Driver.
Name:		ipw2100-firmware
Version:	1.1
Release:	01
License:	distributable
Group:		System Environment/Kernel
URL:		http://ipw2100.sourceforge.net/firmware.php
Source0:	http://cache-www.intel.com/cd/00/00/09/63/96377_96377.zip
# Source0-md5:	817b987a89e811b87384968ffe15615f
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This package contins the firmware for the ipw-2100 driver. Usage of
the firmware is subject to the terms contained in
%{_defaultdocdir}/%{name}-%{version}/LICENSE. Please read the license
carefully.

%prep
%setup -q -c
gunzip -c ipw2100-fw-%{version}.tgz | tar -xf -

%install
rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}
install -d %{buildroot}%{_sysconfdir}/firmware
install -d %{buildroot}%{_libdir}/hotplug/firmware
install -p *.fw %{buildroot}%{_sysconfdir}/firmware/
cd %{buildroot}%{_sysconfdir}/firmware
for file in *.fw; do
  ln -s %{_sysconfdir}/firmware/$file %{buildroot}%{_libdir}/hotplug/firmware/
done

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_sysconfdir}/firmware/*.fw
%{_libdir}/hotplug/firmware/*.fw
