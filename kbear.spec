%define		_beta	beta2
Summary:	kbear - KDE ftp client
Summary(pl):	Klient ftp oparty o KDE
Name:		kbear
Version:	2.0
Release:	%{_beta}.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://prdownloads.sourceforge.net/kbear/%{name}-%{version}%{_beta}.src.tar.bz2
URL:		http://kbear.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
A graphical FTP client for KDE with ability to connect to multiple
hosts simultanously. With KBear you can copy/move files or folders
between hosts with drag and drop or cut and paste. It also has a
flexible site database.

%description -l pl
Graficzny klient FTP dla KDE z mo¿liwo¶ci± jednoczesnego ³±czenia z
wieloma serwerami. KBear pozwala kopiowaæ/przenosiæ pliki lub foldery
miêdzy serwerami przez drag-and-drop lub wytnij-wklej. Ma te¿ bazê
danych o serwerach.

%package devel
Summary:	kbear - KDE ftp client
Summary(pl):	Klient ftp oparty o KDE
Group:		X11/Development/Tools
Requires:	%{name} = %{version}

%description devel
A graphical FTP client for KDE with ability to connect to multiple
hosts simultanously. With KBear you can copy/move files or folders
between hosts with drag and drop or cut and paste. It also has a
flexible site database.

%description -l pl devel
Graficzny klient FTP dla KDE z mo¿liwo¶ci± jednoczesnego ³±czenia z
wieloma serwerami. KBear pozwala kopiowaæ/przenosiæ pliki lub foldery
miêdzy serwerami przez drag-and-drop lub wytnij-wklej. Ma te¿ bazê
danych o serwerach.

%prep
%setup -q -n %{name}-%{version}%{_beta}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"
%configure

# ac/am is broken - don't try to rebuild
touch aclocal.m4 stamp-h.in configure Makefile.in kbear/Makefile.in

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/FTP

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network/FTP}/kbear.desktop

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog KNOWN_BUGS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kbear
%{_datadir}/apps/kbearfilesyspart/*.rc
%{_datadir}/apps/kbearsitemanager/kpartplugins/*.rc
%{_datadir}/apps/konqiconview/kpartplugins/*.rc
%{_datadir}/apps/konqlistview/kpartplugins/*.rc
%{_datadir}/services/kbearftp.protocol
%{_applnkdir}/Network/FTP/kbear.desktop
%{_pixmapsdir}/*/*/apps/*
%{_pixmapsdir}/*/*/actions/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/kbear/*.h
%{_libdir}/*.la
%{_libdir}/kde3/*.la
