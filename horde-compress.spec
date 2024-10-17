%define prj    Horde_Compress

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-compress
Version:       0.0.2
Release:       4
Summary:       Horde Compression API
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-util
Requires:      php-pear
Requires:      php-gettext
Requires:      php-zlib
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



%changelog
* Mon Jul 26 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2011.0
+ Revision: 560539
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 524817
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version to 2

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 509399
- removed BuildRequires: horde-ramework
  replace PreReq with Requires(pre)
- import horde-compress


* Tue Mar  3 2009 Richard Bos <rbos@opensuse.org> - 0.0.2
- Change dependency to horde-framework from just horde
* Mon Dec 22 2008 Richard Bos <rbos@opensuse.org> - 0.0.2
- Changed the pear install command, use package.xml instead of the tarbal
* Wed Nov 26 2008 Richard Bos <rbos@opensuse.org> - 0.0.2
- initial version
