Name: pypsrp
Version: 0.4.1
Release: 1%{?dist}
Summary: Python PowerShell Remoting Protocol Client library
License: MIT License
URL: https://github.com/jborean93/pypsrp	
BuildArch: noarch
Source0: https://github.com/jborean93/pypsrp/archive/v0.4.0.tar.gz
	
BuildRequires:  python3-devel

%description
pypsrp is a Python client for the PowerShell Remoting Protocol (PSRP) and Windows Remove Management (WinRM) service. It allows your to execute commands on a remote Windows host from any machine that can run Python.

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}

%files
%{_bindir}/*

%changelog
* Wed Jan 22 2020 Buttetsu Batou <doubledense@gmail.com> 0.4.1-1
- initial version with skeleton rpm spec 

