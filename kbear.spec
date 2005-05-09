Summary:	kbear - KDE FTP client
Summary(pl):	Klient FTP oparty o KDE
Name:		kbear
Version:	2.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/kbear/%{name}-%{version}-1.src.tar.bz2
# Source0-md5:	5ab2ed17353338cbac5fbe968e53d203
URL:		http://kbear.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	kdebase-devel >= 3.2
#BuildRequires:	kdesdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Summary:	kbear - KDE FTP client
Summary(pl):	Klient FTP oparty o KDE
Group:		X11/Development/Tools
Requires:	%{name} = %{version}

%description devel
A graphical FTP client for KDE with ability to connect to multiple
hosts simultanously. With KBear you can copy/move files or folders
between hosts with drag and drop or cut and paste. It also has a
flexible site database.

%description devel -l pl
Graficzny klient FTP dla KDE z mo¿liwo¶ci± jednoczesnego ³±czenia z
wieloma serwerami. KBear pozwala kopiowaæ/przenosiæ pliki lub foldery
miêdzy serwerami przez drag-and-drop lub wytnij-wklej. Ma te¿ bazê
danych o serwerach.

%prep
%setup -q -n %{name}-2.1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

# ac/am is broken - don't try to rebuild
touch aclocal.m4 stamp-h.in configure Makefile.in kbear/Makefile.in

# UGLY hack
# kto¶ wie jak to zapisaæ w makefile.* jako patch ?? 
for i in `find . -name '*.ui'`; do echo $i; a=`echo $i|sed 's/\.ui$//g'`; uic $i -o ${a}.h;done
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Internet/kbear.desktop $RPM_BUILD_ROOT%{_desktopdir}

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
%{_libdir}/*.la
%{_libdir}/kde3/*.la
%{_datadir}/apps/kbear
%{_datadir}/apps/kbeardirsynchpart
%{_datadir}/apps/kbearfilesyspart
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*/*/apps/*
%{_pixmapsdir}/*/*/actions/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/kbear/*.h
