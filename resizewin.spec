Name:		resizewin
Version:	1.0
Release:	1
Summary:	detect and set the size of the terminal window

Group:		Applications/Text
License:	BSD
URL:		https://github.com/teknoraver/resizewin
Source:		https://github.com/teknoraver/%{name}/archive/refs/heads/master.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	make, gcc

%description
queries the terminal emulator for the current window size and updates
the kernel about it. It is useful when the terminal window is resized
or when its size can't be detected, e.g. in serial lines.

%prep
%setup -q -n %{name}-master

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
cp -p resizewin %{buildroot}%{_bindir}/
cp -p resizewin.1 %{buildroot}%{_mandir}/man1/

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/resizewin
%{_mandir}/man1/resizewin.1*

%changelog
* Wed Mar 5 2025 Matteo Croce <teknoraver@meta.com>
- Initial package
