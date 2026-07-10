%global tl_name epigram
%global tl_revision 20513

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Display short quotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/misc/epigram.tex
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epigram.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package determines (on the basis of the width of the text of the
epigram, laid out on a single line) whether to produce a line or a
displayed paragraph.

