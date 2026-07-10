%global tl_name documentation
%global tl_revision 34521

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Documentation support for C, Java and assembler code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/documentation
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/documentation.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/documentation.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/documentation.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple means of typesetting computer programs
such that the result is acceptable for inclusion in reports, etc.

