Name: mkchroot
Version: 1.0
Release: 1%{?dist}
Summary: Create a basic chroot environment

Group: System Environment/Base
License: MIT
URL: https://github.com/irasnyd/mkchroot
Source0: mkchroot
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: bash
Requires: coreutils
Requires: gawk
Requires: glibc-common

%description
Create a basic chroot environment by copying binaries and their library
dependencies into a directory.

%prep
%setup -T -c -n %{name}-%{version}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/%{name}

%changelog
* Thu Oct 15 2015 Ira W. Snyder <isnyder@lcogt.net> - 1.0-1
- Initial build.
