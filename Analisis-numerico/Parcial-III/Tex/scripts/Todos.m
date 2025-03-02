format rational

% Creamos la función f
f = @(x) 4 ./ (1 + x.^2);

% Parámetros de la integral y el método
a = 0;
b = 1;
valores_n = [10, 50, 100, 250, 500, 1000, 1500, 2000];
I_exacto = pi; 

% Se crea un vector para guardar los errores
errores_puntomedio = zeros(size(valores_n));

% Método del punto medio
for k = 1:length(valores_n)
    n = valores_n(k);
    % Aquí se encuentra el tamaño del intervalo
    h = (b - a) / n; 
    % Se calculan los puntos medios y los guarda en el vector x_medios
    x_medios = a + ((2*(0:1:n-1)+1)*h)/2;
    % Regla del punto medio compuesta
    I_punto_medio = h * sum(f(x_medios)); 
    % Calculo del error
    errores_puntomedio(k) = abs(I_punto_medio - I_exacto);
end

% Se crea un vector para guardar los errores
errores_trapecio = zeros(size(valores_n));

% Método del trapecio
tic;
for k = 1:length(valores_n)
    n = valores_n(k);
    h = (b - a) / n;
    % Extremos de la partición
    x_extremos = a:h:b;
    m = length(x_extremos);

    % Aplicar la regla del trapecio compuesta
    I_trapecio = (h/2) * (f(a) + 2*sum(f(x_extremos(2:m-1))) + f(b));

    % Calculo del error
    errores_trapecio(k) = abs(I_trapecio - I_exacto);
end

% Se crea un vector para guardar los errores
errores_simpson = zeros(size(valores_n));

% Método de Simpson
tic;
for k = 1:length(valores_n)
    n = valores_n(k);
    
    % Aquí nos aseguramos que n sea par (Simpson necesita n par)
    if mod(n, 2) == 1
        n = n + 1;
    end
    
    h = (b - a) / n;
    % Extremos de la partición
    x_extremos = a:h:b;
    m = length(x_extremos);

    % Aplicar la regla de Simpson compuesta
    I_simpson = (h/3) * (f(a) + 4*sum(f(x_extremos(2:2:m-1))) + 2*sum(f(x_extremos(3:2:m-2))) + f(b));

    % Calculo del error
    errores_simpson(k) = abs(I_simpson - I_exacto);
end

% Graficamos los errores en una sola figura
figure;
loglog(valores_n, errores_puntomedio, 'o-', 'LineWidth', 2, 'DisplayName', 'Punto Medio');
hold on;
loglog(valores_n, errores_trapecio, 's-', 'LineWidth', 2, 'DisplayName', 'Trapecio');
loglog(valores_n, errores_simpson, 'd-', 'LineWidth', 2, 'DisplayName', 'Simpson');
hold off;

% Configuraciones de la gráfica
xlabel('Número de subintervalos (n)');
ylabel('Error absoluto');
title('Comparación de Métodos de Integración Numérica');
legend;
grid on;
