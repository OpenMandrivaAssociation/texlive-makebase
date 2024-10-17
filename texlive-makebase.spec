Name:		texlive-makebase
Version:	41012
Release:	2
Summary:	Typeset counters in a different base
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makebase
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebase.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebase.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebase.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package typesets a LaTeX counter such as page in an
arbitrary base (default 16). It does not change font or
typeface. The package extends the functionality of the existing
hex LaTeX 2.09 package and provides documentation. However, the
author is not a mathematician, and suggestions for rewriting
the code are welcomed. Warning: this is alpha software and may
contain bugs. Please report problems to the author.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/makebase
%{_texmfdistdir}/tex/latex/makebase
%doc %{_texmfdistdir}/doc/latex/makebase

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
