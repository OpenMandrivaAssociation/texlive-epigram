# revision 20513
# category Package
# catalog-ctan /macros/generic/misc/epigram.tex
# catalog-date 2010-11-20 18:15:00 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-epigram
Version:	20101120
Release:	1
Summary:	Display short quotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/misc/epigram.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigram.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
The package determines (on the basis of the width of the text
of the epigram, laid out on a single line) whether to produce a
line or a displayed paragraph.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/epigram/epigram.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
