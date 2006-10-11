# TODO: wait for mono-basic usable with just mono, without MSVC
Summary:	MonoBASIC compiler for mono
Summary(pl):	Kompilator MonoBASIC dla mono
Name:		mono-basic
Version:	1.1.17
Release:	0.1
License:	MIT-like
Group:		Development/Languages
#Source0Download: http://go-mono.com/sources-stable/
Source0:	http://go-mono.com/sources/mono-basic/%{name}-%{version}.zip
# no sense to fill distfiles now, it still requires MSVS
# NoSource0-md5:	0a32a7b12b90e35249caefb3e85c4245
URL:		http://www.mono-project.org/
BuildRequires:	mono-csharp
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MonoBASIC compiler for mono.

%description -l pl
Kompilator MonoBASIC dla mono.

%package runtime
Summary:	MonoBASIC runtime library
Summary(pl):	Biblioteka uruchomieniowa MonoBASIC
Group:		Libraries

%description runtime
MonoBASIC runtime library.

%description runtime -l pl
Biblioteka uruchomieniowa MonoBASIC.

%prep
%setup -q

%build
# TODO

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files runtime
%defattr(644,root,root,755)
%doc vbruntime/TODO.txt
