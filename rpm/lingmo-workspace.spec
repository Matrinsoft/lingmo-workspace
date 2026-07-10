Name:           lingmo-workspace
Version:        1.0.0
Release:        1%{?dist}
Summary:        Lingmo Workspace

License:        GPL-3.0-or-later
URL:            https://github.com/lingmo-os/lingmo-workspace
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.20
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel >= 6.5
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel

%description
Lingmo Workspace for Lingmo Desktop.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md

%changelog
* Wed Jul 10 2026 Lingmo OS Team <team@lingmo.org> - 1.0.0-1
- Initial release
