Name: pypsrp
Version: 0.4.0
Release: 1%{?dist}
Summary: Python PowerShell Remoting Protocol Client library
License: MIT License
URL: https://github.com/jborean93/pypsrp	
BuildArch: noarch
Source0: https://github.com/jborean93/pypsrp/archive/v0.4.0.tar.gz
	
BuildRequires:  python3-devel
	
%global _description %{expand:
pypsrp is a Python client for the PowerShell Remoting Protocol (PSRP) and Windows Remove Management (WinRM) service. It allows your to execute commands on a remote Windows host from any machine that can run Python.}
 
%description %_description
	
%package     -n python3-pypsrp
Summary:        %summary
%description -n python3-pypsrp %_description

%prep
%autosetup -n %{name}-%{version}
rm -rf %{py3dir} && cp -a . %{py3dir}

%build	
pushd %{py3dir}
%{py3_build}

%install
pushd %{py3dir}
%{py3_install}

%files -n python3-pypsrp
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/pypsrp-%{version}*.egg-info
%{python3_sitelib}/pypsrp

%changelog
* Wed Jan 22 2020 Buttetsu Batou <doubledense@gmail.com> 0.4.0-1
- new package



