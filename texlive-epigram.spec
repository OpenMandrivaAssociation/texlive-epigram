# revision 20513
# category Package
# catalog-ctan /macros/generic/misc/epigram.tex
# catalog-date 2010-11-20 18:15:00 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-epigram
Version:	20101120
Release:	2
Summary:	Display short quotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/misc/epigram.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigram.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101120-2
+ Revision: 751492
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101120-1
+ Revision: 718343
- texlive-epigram
- texlive-epigram
- texlive-epigram
- texlive-epigram

