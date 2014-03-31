Name:       pacrunner

Summary:    Proxy configuration daemon
Version:    0.8
Release:    1
Group:      System/Networking
License:    GPLv2
URL:        http://connman.net/
Source0:    http://www.kernel.org/pub/linux/network/connman/pacrunner-%{version}.tar.xz
Source1:    libproxy.py
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  python
BuildRequires:  pkgconfig(gthread-2.0)
Provides:   libproxy
Obsoletes:   libproxy < 0.5

%description
PacRunner provides a daemon for processing proxy configuration
and providing information to clients over D-Bus.


%package python
Summary:    Python lib for PacRunner
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   pacrunner
Provides:   libproxy-python
Obsoletes:   libproxy-python < 0.5

%description python
A python library for proxy configuration and autodetection

%package devel
Summary:    Development files for PacRunner
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Provides:   libproxy-devel
Obsoletes:   libproxy-devel < 0.5

%description devel
This provides the development files for building against
pacrunner's implementation of libproxy
#'

%package test
Summary:    Test files for PacRunner
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description test
This provides the test files for pacrunner

%package plugin-devel
Summary:    Development files to develop PacRunner plugins
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
%description plugin-devel
%{summary}

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./bootstrap

%configure --disable-static \
    --enable-libproxy \
    --disable-capng \
    --enable-plugindevel \
    --enable-datafiles 

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

mv $RPM_BUILD_ROOT/%{_datadir}/dbus-1/system-services/{,org.}pacrunner.service
mkdir -p ${RPM_BUILD_ROOT}/%{python_sitelib}
install -m0644 %{SOURCE1} $RPM_BUILD_ROOT/%{python_sitelib}/libproxy.py
rm -f $RPM_BUILD_ROOT/%{_libdir}/libproxy.la


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README COPYING.LIB AUTHORS ChangeLog
%{_sbindir}/pacrunner
%{_libdir}/libproxy.so.1.0.0
%{_libdir}/libproxy.so.1
%{_bindir}/proxy
%{_datadir}/dbus-1/system-services/org.pacrunner.service
%config %{_sysconfdir}/dbus-1/system.d/pacrunner.conf

%files python
%defattr(-,root,root,-)
%{python_sitelib}/libproxy.py*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libproxy.so
%{_includedir}/proxy.h
%{_libdir}/pkgconfig/libproxy-1.0.pc

%files test
%defattr(-,root,root,-)
%{_bindir}/manual-proxy-test

%files plugin-devel
%defattr(-,root,root,-)
%{_includedir}/pacrunner/js.h
%{_includedir}/pacrunner/plugin.h
%{_libdir}/pkgconfig/pacrunner-1.0.pc
