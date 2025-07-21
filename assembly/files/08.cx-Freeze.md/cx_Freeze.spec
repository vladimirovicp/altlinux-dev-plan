Name: python3-module-cx_Freeze
Version: 8.3.0
Release: alt1
Summary: cx_Freeze — cross-platform executable builder for Python

License: PSF-2.0
Group: Development/Python
Url: https://github.com/marcelotduarte/cx_Freeze

Source: cx_Freeze-8.3.0.tar.gz
BuildArch: x86_64

BuildRequires: python3-module-setuptools
BuildRequires: python3-devel
BuildRequires: python3-module-packaging
BuildRequires: python3-module-filelock

%description
cx_Freeze is a set of utilities for freezing Python scripts into executables.

%prep
%setup -q -n cx_Freeze-8.3.0
%{__sed} -i 's/^license = "PSF-2.0"$/license = {text = "PSF-2.0"} /' pyproject.toml
%{__sed} -i '/^license-files =/d' pyproject.toml

%build
%pyproject_build

%install
rm -rf %{buildroot}
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/cx_Freeze
%_bindir/cxfreeze

%changelog
* Fri Jul 18 2025 Joe Hacker <joe@email.address> 8.3.0-alt1
- Add BuildRequires tag
