%define origname BeautifulSoup 
  
Name:           python-beautifulsoup 
Version:        3.0.3
Release:        %mkrel 1
Summary:        The Screen-Scraper's Friend 
  
Group:          Development/Libraries 
License:        PSF 
URL:            http://www.crummy.com/software/BeautifulSoup 
Source0:        http://www.crummy.com/software/BeautifulSoup/download/%{origname}.py 
  
BuildArch:      noarch 
BuildRequires:  python-devel 
Requires:       python 
  
%description 
The BeautifulSoup class turns arbitrarily bad HTML into a tree-like 
nested tag-soup list of Tag objects and text snippets. A Tag object 
corresponds to an HTML tag.  It knows about the HTML tag's attributes, 
and contains a representation of everything contained between the 
original tag and its closing tag (if any). It's easy to extract Tags 
that meet certain criteria. 
  
%prep 
  
%build 
  
%install 
rm -rf $RPM_BUILD_ROOT 
  
TARGETDIR=$RPM_BUILD_ROOT%{python_sitelib}
mkdir -p $TARGETDIR 
cp %{SOURCE0} $TARGETDIR 
%{__python} %{_libdir}/python%{pyver}/compileall.py -f $TARGETDIR/* 
   
%clean 
rm -rf $RPM_BUILD_ROOT 
  
%files  
%defattr(-,root,root,-) 
%{python_sitelib}/%{origname}.py 


