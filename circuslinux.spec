Summary:	"Circus Linux!" is a clone of the Atari 2600 game "Circus Atari"
Summary(pl):	"Circus Linux!" jest klonem gry z Atari 2600 "Circus Atari"
Name:		circuslinux
Version:	1.0.3
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/circus-linux/%{name}-%{version}.tar.gz
# Source0-md5:	d53f7d28d974c5605d6bebb9b1569216
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-version.patch
URL:		http://www.newbreedsoftware.com/circus-linux/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
"Circus Linux!" is a clone of the Atari 2600 game "Circus Atari", which is
itself a clone of an earlier arcade game named, simply "Circus".

The object is to move a teeter-totter back and forth across the screen
to bounce clowns up into the air. When they reach the top, they pop
rows of balloons and then fall back down.

(The gameplay is similar to the classics "Breakout" and "Arkanoid.")

%description -l pl
"Circus Linux!" jest klonem gry z Atari 2600 - "Circus Atari", która z
kolei sama jest klonem wcze¶niejszej gry zrêczno¶ciowej, nazywaj±cej siê
po prostu "Circus".

Celem gry jest przesuwanie hu¶tawki w poprzek ekranu tak aby podbijaæ
skacz±cych clownów do góry. Kiedy clown wyskakuje, zbija czê¶æ z baloników
lataj±cych w rzêdach pod sufitem, a potem spada z powrotem na dó³.

Motyw gry jest podobny do klasycznych gier - "Breakout" i "Arkanoid"

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Arcade,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES.txt FAQ.txt README.txt README-SDL.txt TODO.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/Games/Arcade/*
%{_pixmapsdir}/*
