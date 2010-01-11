
%define		qtver	4.6.0
%define		kde4ver	4.3.80
%define		svnsnap	1058941
%define		orgname	kbluetooth

Summary:	KDE Bluetooth framework
Summary(pl.UTF-8):	Podstawowe środowisko KDE Bluetooth
Name:		kde4-kdebluetooth
Version:	0.4
Release:	1.%{svnsnap}.1
License:	GPL
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/kde-bluetooth/%{origname}-%{version}.tar.bz2
# get via: svn co svn://anonsvn.kde.org/home/kde/trunk/playground/network/kbluetooth
Source0:	%{orgname}-%{version}-%{svnsnap}.tar.bz2
# Source0-md5:	77ff139629c35bbb17b33f7012b2c02c
URL:		http://bluetooth.kmobiletools.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.3
BuildRequires:	kde4-kdebase-workspace-devel >= %{kde4ver}
BuildRequires:	kde4-kdelibs-devel >= %{kde4ver}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	shared-desktop-ontologies-devel >= 0.2
BuildRequires:	soprano-devel >= 2.3.70
Requires:	obex-data-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KDE Bluetooth Framework is a set of tools built on top of Linux'
Bluetooth stack BlueZ. Its goal is to provide easy access to the most
common Bluetooth profiles and to make data exchange with Bluetooth
enabled phones and PDAs as straightforward as possible

%description -l pl.UTF-8
Projekt KDE Bluetooth jest zestawem narzędzi zbudowanych na górnej
warstwie stosu Bluetooth BlueZ. Jego celem jest dostarczenie łatwego
dostępu do większości profili Bluetooth oraz wymiany danych z
telefonami komórkowymi z Bluetooth oraz PDA tak bezpośrednio jak to
jest możliwe.

%prep
%setup -q -n %{orgname}-%{version}-%{svnsnap}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/%{orgname}*
%{_desktopdir}/kde4/%{orgname}.desktop
%{_iconsdir}/hicolor/*/apps/%{orgname}*.png
