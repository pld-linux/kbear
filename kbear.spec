Summary:	kbear - KDE ftp client
Summary(pl):	Klient ftp oparty o KDE
Name:		kbear
Version:	1.2.1
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/kbear/%{name}-%{version}.src.tar.bz2
Patch0:		%{name}-headers.patch
URL:		http://kbear.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
A graphical FTP client for KDE2 with ability to connect to multiple
hosts simultanously. With KBear you can copy/move files or folders
between hosts with drag and drop or cut and paste. It also has a
flexible site database.

%description -l pl
Graficzny klient FTP dla KDE2 z mo¿liwo¶ci± jednoczesnego ³±czenia z
wieloma serwerami. KBear pozwala kopiowaæ/przenosiæ pliki lub foldery
miêdzy serwerami przez drag-and-drop lub wytnij-wklej. Ma te¿ bazê
danych o serwerach.

%prep
%setup -q
%patch -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"
%configure2_13

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kbear
%{_applnkdir}/Network/FTP/kbear.desktop
%{_pixmapsdir}/*/*/apps/*
