
%define		qtver	4.6.3
%define		kde4ver	4.5.0
%define		svnsnap	1162777
%define		orgname	kbluetooth

Summary:	KDE Bluetooth framework
Summary(pl.UTF-8):	Podstawowe środowisko KDE Bluetooth
Name:		kde4-kdebluetooth
Version:	1.0
Release:	0.%{svnsnap}.1
License:	GPL
Group:		X11/Applications
#Source0:	http://opendesktop.org/CONTENT/content-files/112110-%{orgname}-%{version}.tar.bz2
# get via: svn co svn://anonsvn.kde.org/home/kde/trunk/playground/network/kbluetooth
Source0:	%{orgname}-%{version}-%{svnsnap}.tar.bz2
# Source0-md5:	834c93a3adb8d340c1cc03d701b5b476
URL:		http://techbase.kde.org/Kbluetooth
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-tools
BuildRequires:	kde4-kdebase-workspace-devel >= %{kde4ver}
BuildRequires:	kde4-kdelibs-devel >= %{kde4ver}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	shared-desktop-ontologies-devel >= 0.2
BuildRequires:	soprano-devel >= 2.4.0.1
Requires:	obex-data-server
Requires:	bluez
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

#%find_lang %{orgname} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

#%%files -f %{orgname}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/kbluetooth
%attr(755,root,root) %{_bindir}/kbluetooth-devicemanager
%attr(755,root,root) %{_bindir}/kbluetooth-wizard
%{_desktopdir}/kde4/kbluetooth.desktop
%{_datadir}/apps/kbluetooth-wizard
%{_iconsdir}/hicolor/*/apps/kbluetooth.png
%{_iconsdir}/hicolor/*/apps/kbluetooth-flashing.png
