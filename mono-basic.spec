Summary:	MonoBASIC compiler for mono
Summary(pl.UTF-8):	Kompilator MonoBASIC dla mono
Name:		mono-basic
Version:	2.6
Release:	1
License:	MIT-like/LGPL
Group:		Development/Languages
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/mono-basic/%{name}-%{version}.tar.bz2
# Source0-md5:	64248ca51cd09fb53e34b0373f5dfd91
URL:		http://www.mono-project.com/
BuildRequires:	mono-csharp
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Visual Basic.Net(TM) compiler for mono.

%description -l pl.UTF-8
Kompilator Visual Basic.Net(TM) dla mono.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vbnc
%{_mandir}/man1/vbnc.1*
%{_prefix}/lib/mono/2.0/*
%exclude %{_prefix}/lib/mono/2.0/*.mdb
%{_prefix}/lib/mono/gac/Microsoft.VisualBasic
%exclude %{_prefix}/lib/mono/gac/*/*/*.mdb
