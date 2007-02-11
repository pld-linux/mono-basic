Summary:	MonoBASIC compiler for mono
Summary(pl):	Kompilator MonoBASIC dla mono
Name:		mono-basic
Version:	1.2.3
Release:	1
License:	MIT-like/LGPL
Group:		Development/Languages
Source0:	http://go-mono.com/sources/mono-basic/%{name}-%{version}.tar.gz
# Source0-md5:	8cd1473154ca2edfb3220721eadc3e0f
URL:		http://www.mono-project.org/
BuildRequires:	mono-csharp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Visual Basic.Net(TM) compiler for mono.

%description -l pl
Kompilator Visual Basic.Net(TM) dla mono.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
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
%{_prefix}/lib/mono/2.0/*
%exclude %{_prefix}/lib/mono/2.0/*.mdb
%{_prefix}/lib/mono/gac/Microsoft.VisualBasic
%exclude %{_prefix}/lib/mono/gac/*/*/*.mdb
