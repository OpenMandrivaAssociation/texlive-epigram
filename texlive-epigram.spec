Name:		texlive-epigram
Version:	20513
Release:	1
Summary:	Display short quotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/misc/epigram.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigram.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package determines (on the basis of the width of the text
of the epigram, laid out on a single line) whether to produce a
line or a displayed paragraph.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/epigram/epigram.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
