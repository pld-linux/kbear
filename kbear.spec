Name: kbear
Summary: kbear
Version: 1.2
Release: 1
Source: /usr/src/redhat/SOURCES/kbear-1.2.src.tar.bz2
Group: Applications/Internet
BuildRoot: /var/tmp/build-root-%{name}
Copyright: GPL
Packager: Björn Sahlström
Distribution: 7
Prefix: /usr --with-qt-dir=/usr/lib/qt-2.2.2
Url: http://www.kbear.org/
Vendor: Redhat
%description
A graphical FTP client for KDE2 with ability to connect to multiple hosts simultanously.
With KBear you can copy/move files or folders between hosts with drag and drop or cut and paste.
It also has a flexible site database.
%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT
%setup -q
%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make -j 2
%install
make DESTDIR=$RPM_BUILD_ROOT install-strip

cd $RPM_BUILD_ROOT

find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}
%defattr(-,root,root,0755)
