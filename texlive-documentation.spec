Name:		texlive-documentation
Version:	34521
Release:	2
Summary:	Documentation support for C, Java and assembler code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/documentation
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/documentation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/documentation.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/documentation.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a simple means of typesetting computer
programs such that the result is acceptable for inclusion in
reports, etc.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/documentation/documentation.sty
%doc %{_texmfdistdir}/doc/latex/documentation/README
%doc %{_texmfdistdir}/doc/latex/documentation/documentation.pdf
#- source
%doc %{_texmfdistdir}/source/latex/documentation/documentation.dtx
%doc %{_texmfdistdir}/source/latex/documentation/documentation.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
