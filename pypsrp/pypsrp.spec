Name: pypsrp
Version: 0.4.0
Release: 1%{?dist}
Summary: Python PowerShell Remoting Protocol Client library
Group: Development/Tools
License: MIT License
URL: https://github.com/jborean93/pypsrp	
BuildArch: noarch
Source0: https://github.com/jborean93/pypsrp/archive/v0.4.0.tar.gz

%description
pypsrp is a Python client for the PowerShell Remoting Protocol (PSRP) and Windows Remove Management (WinRM) service. It allows your to execute commands on a remote Windows host from any machine that can run Python.

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/stern

%files
%{_bindir}/*

%changelog
* Fri Jan 3 2020 Eduardo Minguez <edu@redhat.com> - 1.11.0-1
- Bump version

* Fri Jun 21 2019 Eduardo Minguez <edu@redhat.com> - 1.10.0-1
- First version
