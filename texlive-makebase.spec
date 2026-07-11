%global tl_name makebase
%global tl_revision 41012

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Typeset counters in a different base
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makebase
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makebase.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makebase.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makebase.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package typesets a LaTeX counter such as page in an arbitrary base
(default 16). It does not change font or typeface. The package extends
the functionality of the existing hex LaTeX 2.09 package and provides
documentation. However, the author is not a mathematician, and
suggestions for rewriting the code are welcomed. Warning: this is alpha
software and may contain bugs. Please report problems to the author.

