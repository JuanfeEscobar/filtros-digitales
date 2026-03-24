clc; clear; close all;

% Parámetros
fs = 500;              % Frecuencia de muestreo
t = 0:1/fs:1-1/fs;     % Vector de tiempo

% Señal compuesta (10 Hz y 50 Hz)
signal = sin(2*pi*10*t) + 0.5*sin(2*pi*50*t);

% Ruido
noise = 0.5*randn(size(t));

% Señal con ruido
signal_noisy = signal + noise;

% Graficar señal original con ruido
figure;
plot(t, signal_noisy);
title('Señal con ruido');
xlabel('Tiempo');
ylabel('Amplitud');
grid on;

% Filtro pasa bajos
fc_lp = 30; % Frecuencia de corte

[b_lp, a_lp] = butter(4, fc_lp/(fs/2), 'low');
filtered_lp = filter(b_lp, a_lp, signal_noisy);

% Filtro pasa altos
fc_hp = 20;

[b_hp, a_hp] = butter(4, fc_hp/(fs/2), 'high');
filtered_hp = filter(b_hp, a_hp, signal_noisy);

% Filtro pasa bandas (20 Hz a 40 Hz)
fc_bp = [20 40];

[b_bp, a_bp] = butter(4, fc_bp/(fs/2), 'bandpass');
filtered_bp = filter(b_bp, a_bp, signal_noisy);

figure;

subplot(4,1,1);
plot(t, signal_noisy);
title('Señal con ruido');

subplot(4,1,2);
plot(t, filtered_lp);
title('Filtro Pasa Bajos');

subplot(4,1,3);
plot(t, filtered_hp);
title('Filtro Pasa Altos');

subplot(4,1,4);
plot(t, filtered_bp);
title('Filtro Pasa Bandas');

figure;
freqz(b_lp, a_lp, 1024, fs);
title('Respuesta en frecuencia - Pasa Bajos');

figure;
freqz(b_hp, a_hp, 1024, fs);
title('Respuesta en frecuencia - Pasa Altos');

figure;
freqz(b_bp, a_bp, 1024, fs);
title('Respuesta en frecuencia - Pasa Bandas');
