%define prj    Horde_Compress

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-compress
Version:       0.0.2
Release:       %mkrel 1
Summary:       Horde Compression API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
PreReq:        %{_bindir}/pear
Requires:      horde-util
Requires:      php-pear
Requires:      php-gettext
Requires:      php-zlib
BuildRequires: horde-framework
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde
BuildRoot:     %{_tmppath}/%{name}-%{version}

%description
These classes provide functionality useful for all kind of applications.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Compress
%{peardir}/Horde/Compress.php
%{peardir}/Horde/Compress/dbx.php
%{peardir}/Horde/Compress/gzip.php
%{peardir}/Horde/Compress/tar.php
%{peardir}/Horde/Compress/tnef.php
%{peardir}/Horde/Compress/zip.php

