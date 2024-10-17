%define name    ocropus
%define version 0.1.1
%define svn	681
%define release %mkrel %svn.2

Name:           %{name} 
Summary:        Pluggable, scripable OCR system
Version:        %{version} 
Release:        %{release} 
Source0:        %{name}-%{svn}.tar.bz2
URL:            https://code.google.com/p/ocropus/

Group:          Office
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:        Apache
BuildRequires:	tesseract-devel >= 2.01
BuildRequires:  png-devel jpeg-devel tiff-devel
BuildRequires:	aspell-devel
BuildRequires:	SDL-devel SDL_image-devel SDL_gfx-devel
BuildRequires:	editline-devel
BuildRequires:	openfst-devel
BuildRequires:	lua-devel
BuildRequires:	tolua++-devel
BuildRequires:	ftjam
Requires:	tesseract

%description
OCRopus(tm) is a state-of-the-art document analysis and OCR system, featuring
pluggable layout analysis, pluggable character recognition, statistical
natural language modeling, and multi-lingual capabilities.

%prep
%setup -q -n %name
perl -pi -e 's/CPPFLAGS/CXXFLAGS/g' Jamfile.in

%build 
%configure --with-tesseract=%_prefix
jam

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
install -m 0755 ocrocmd/ocrocmd %buildroot/%_bindir
install -m 0755 ocroscript/ocroscript %buildroot/%_bindir
install -m 0755 ocroscript/ocroscript-simple %buildroot/%_bindir

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root) 
%doc README CHANGES COPYING
%{_bindir}/*

