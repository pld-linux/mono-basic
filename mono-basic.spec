Summary:	MonoBASIC compiler for mono
Summary(pl.UTF-8):	Kompilator MonoBASIC dla mono
Name:		mono-basic
Version:	2.8
Release:	1
License:	MIT-like/LGPL
Group:		Development/Languages
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/mono-basic/%{name}-%{version}.tar.bz2
# Source0-md5:	b4fec9875353ce0aeeb27d795bfa1d58
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
%{_prefix}/lib/mono/2.0/Microsoft.VisualBasic.dll
%{_prefix}/lib/mono/2.0/Mono.Cecil.VB.dll
%{_prefix}/lib/mono/2.0/Mono.Cecil.VB.Mdb.dll
%{_prefix}/lib/mono/2.0/Mono.Cecil.VB.Pdb.dll
%{_prefix}/lib/mono/2.0/vbnc.exe
%{_prefix}/lib/mono/2.0/vbnc.rsp
%{_prefix}/lib/mono/gac/Microsoft.VisualBasic
%{_prefix}/lib/mono/gac/Mono.Cecil.VB
%{_prefix}/lib/mono/gac/Mono.Cecil.VB.Mdb
%{_prefix}/lib/mono/gac/Mono.Cecil.VB.Pdb
%exclude %{_prefix}/lib/mono/gac/*/*/*.mdb
