Summary:	XBase64 - xbase-compatible C++ class library
Summary(pl.UTF-8):	XBase64 - kompatybilna z xbase biblioteka klas C++
Name:		xbase64
Version:	3.1.2
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (programs)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/xdb/%{name}-%{version}.tar.gz
# Source0-md5:	7f3a727c142b4339faa781e1f6d5871c
Patch0:		%{name}-fix.patch
Patch1:		%{name}-am.patch
URL:		http://linux.techass.com/projects/xdb/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XBase64 is an xbase (i.e. dBase, FoxPro, etc.) compatible C++ class
library. It's useful for accessing data in legacy dBase 3 and 4
database files as well as a general light-weight database engine. It
includes support for DBF (dBase version 3 and 4) data files, NDX and
NTX indexes, and DBT (dBase version 3 and 4). It supports file and
record locking under *nix OSes.

%description -l pl.UTF-8
XBase64 to kompatybilna z xbase (czyli dBase, FoxPro itp.) biblioteka
klas C++. Jest przydatna do dostępu do danych w plikach starych baz
dBase 3 i 4, a także jako lekki silnik baz danych ogólnego
przeznaczenia. Obsługuje pliki baz DBF (dBase w wersji 3 i 4), indeksy
NDX i NTX oraz DBT (dBase w wersji 3 i 4). Obsługuje blokowanie
plików i rekordów pod systemami uniksowymi.

%package devel
Summary:	XBase64 development files
Summary(pl.UTF-8):	Pliki dla programistów używających XBase64
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains XBase64 development files.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne przy tworzeniu
aplikacji używających Xbase64.

%package static
Summary:	Static XBase64 library
Summary(pl.UTF-8):	Statyczna biblioteka XBase64
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XBase64 library.

%description static -l pl.UTF-8
Statyczna biblioteka XBase64.

%package tools
Summary:	XBase64 utilities for xbase files
Summary(pl.UTF-8):	XBase64 - narzędzia do plików xbase
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Obsoletes:	xbase-tools
Conflicts:	xbase < 2.1.1-5

%description tools
XBase64 utilities for xbase files.

%description tools -l pl.UTF-8
XBase64 - narzędzia do plików xbase.

%prep
%setup -q

# not undos - there are some CRs in the middle if lines
%{__sed} -i -e 's,\r,,' -e 's,__GNU LesserG__,__GNU_LesserG__,' xbase64/*.[ch]*

%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-index-ndx \
	--with-index-ntx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog authors news readme todo
%attr(755,root,root) %{_libdir}/libxbase64.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxbase64.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/html/{*.html,*.png}
%attr(755,root,root) %{_bindir}/xbase64-config
%attr(755,root,root) %{_libdir}/libxbase64.so
%{_libdir}/libxbase64.la
%{_includedir}/xbase64

%files static
%defattr(644,root,root,755)
%{_libdir}/libxbase64.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/checkndx
%attr(755,root,root) %{_bindir}/copydbf
%attr(755,root,root) %{_bindir}/dbfutil1
%attr(755,root,root) %{_bindir}/dbfxtrct
%attr(755,root,root) %{_bindir}/deletall
%attr(755,root,root) %{_bindir}/dumphdr
%attr(755,root,root) %{_bindir}/dumprecs
%attr(755,root,root) %{_bindir}/packdbf
%attr(755,root,root) %{_bindir}/reindex
%attr(755,root,root) %{_bindir}/undelall
%attr(755,root,root) %{_bindir}/zap
