# revision 25405
# category Package
# catalog-ctan /macros/latex/contrib/documentation
# catalog-date 2011-12-02 09:08:13 +0100
# catalog-license lppl1.2
# catalog-version 0.1
Name:		texlive-documentation
Version:	0.1
Release:	3
Summary:	Documentation support for C, Java and assembler code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/documentation
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/documentation.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/documentation.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/documentation.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
