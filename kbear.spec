Name:		kbear
Summary:	kbear
Version:	1.2
Release:	1
Source0:	%{name}-%{version}.src.tar.bz2
Group:		Applications/Internet
######		Unknown group!
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
License:	GPL
Url:		http://www.kbear.org/
Vendor:		Redhat

%description
A graphical FTP client for KDE2 with ability to connect to multiple
hosts simultanously. With KBear you can copy/move files or folders
between hosts with drag and drop or cut and paste. It also has a
flexible site database.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}" ./configure --prefix=%{_prefix}
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
