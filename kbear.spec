Summary:	kbear - KDE ftp client
Summary(pl):	Klient ftp oparty o KDE
Name:		kbear
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Networking
# We prefer ftp: URLs if possible
# Source0:	http://prdownloads.sourceforge.net/kbear/%{name}-%{version}.src.tar.bz2
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/kbear/%{name}-%{version}.src.tar.bz2
URL:		http://kbear.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}"
%configure2_13 \
	--prefix=%{_prefix}
%{__make} -j 2

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

cd $RPM_BUILD_ROOT

find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}
%defattr(644,root,root,755)
