%global tl_name luacolor
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.18
Release:	%{tl_revision}.1
Summary:	Color support based on LuaTeXs node attributes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/luacolor
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luacolor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luacolor.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luacolor.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements color support based on LuaTeX's node attributes.

