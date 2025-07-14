%define oname brightness_controller_linux

Name: brightness-controller
Version: 2.4
Release: alt1

Summary: Brightness Controller for Linux
License: GPLv3+
Group: Graphical desktop/GNOME
Url: https://github.com/LordAmit/Brightness

Source:%name-%version.tar
BuildArch: noarch


Requires: python3-module-qtpy
Requires: python3-module-PyQt5
Requires: python3-module-poetry
Requires: rpm-build-python3

%description
Using Brightness Controller? you can control brightness of both primary and external displays in Linux. Check it out!

%prep
%setup -q

%build
cd brightness-controller-linux/
mv README.md readme.md
%pyproject_build

%install
cd brightness-controller-linux/
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%_bindir/brightness-controller

%changelog
* Mon Jul 14 2025 Joe Hacker <joe@email.address> 2.4-alt1
- Initial build for ALT.
