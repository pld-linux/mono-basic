Summary:	MonoBASIC compiler for mono
Summary(pl.UTF-8):	Kompilator MonoBASIC dla mono
Name:		mono-basic
Version:	3.8
Release:	1
License:	MIT (libraries), LGPL v2.1+ (compiler)
Group:		Development/Languages
Source0:	http://download.mono-project.com/sources/mono-basic/%{name}-%{version}.tar.bz2
# Source0-md5:	018b4daf49c55e133b84b8a19fc172e2
URL:		http://www.mono-project.com/
BuildRequires:	mono-csharp >= 3.8
ExclusiveArch:	%{ix86} %{x8664} arm ia64 mips ppc ppc64 s390x sparc sparcv9 sparc64
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
%doc ChangeLog LICENSE README
%attr(755,root,root) %{_bindir}/vbnc
%attr(755,root,root) %{_bindir}/vbnc2
%{_mandir}/man1/vbnc.1*
%{_prefix}/lib/mono/2.0/Microsoft.VisualBasic.dll
%{_prefix}/lib/mono/4.0/Microsoft.VisualBasic.dll
%{_prefix}/lib/mono/4.5/Microsoft.VisualBasic.dll
%{_prefix}/lib/mono/4.5/Mono.Cecil.VB.dll
%{_prefix}/lib/mono/4.5/Mono.Cecil.VB.Mdb.dll
%{_prefix}/lib/mono/4.5/Mono.Cecil.VB.Pdb.dll
%{_prefix}/lib/mono/4.5/vbnc.exe
%{_prefix}/lib/mono/4.5/vbnc.rsp
%exclude %{_prefix}/lib/mono/4.5/vbnc.exe.mdb
%{_prefix}/lib/mono/gac/Microsoft.VisualBasic
%{_prefix}/lib/mono/gac/Mono.Cecil.VB
%{_prefix}/lib/mono/gac/Mono.Cecil.VB.Mdb
%{_prefix}/lib/mono/gac/Mono.Cecil.VB.Pdb
%exclude %{_prefix}/lib/mono/gac/*/*/*.mdb
