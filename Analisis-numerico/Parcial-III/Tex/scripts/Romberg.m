format long
% Definimos la función
f = @(x) 4 ./ (1 + x.^2);
% Límites de integración
a = 0;
b = 1;
% Valor exacto de la integral
I_exacto = pi; 
% Tolerancia
eps = 1e-8;
% Calculamos la integral con Romberg y obtenemos errores
tic;
[I_romberg, hs, errores] = romberg(f, a, b, I_exacto, eps);
toc
% Graficamos log(error) vs log(h)
figure;
loglog(hs, errores, '-o', 'LineWidth', 2);
xlabel('log(h)');
ylabel('log(error)');
title('Error en términos diagonales de la tabla de Romberg');
grid on;
% --- FUNCIONES ---
function [I_romberg, hs, errores] = romberg(f, a, b, I_exacto, eps)
    if nargin < 5
        % Precisión por defecto
        eps = 1e-8; 
    end
    % Matriz de Romberg
    R = zeros(1, 1);
    % Primer trapecio
    R(1,1) = 0.5 * (b - a) * (f(a) + f(b));
    print_row(R(1,1));
    % Inicialización de vectores para la gráfica
    hs = [];
    errores = [];
    % Número de iteraciones
    n = 1; 
    while true
        % Refinamos h
        h = (b - a) / 2^n; 
        % Nueva regla del trapecio
        R(n+1,1) = 0.5 * R(n,1) + h * sum(f(a + (2*(1:2^(n-1)) - 1) * h)); 
        % Extrapolación de Richardson
        for m = 2:n+1
            R(n+1,m) = R(n+1,m-1) + (R(n+1,m-1) - R(n,m-1)) / (4^(m-1) - 1);
        end
        % Imprimir la fila
        print_row(R(n+1, 1:n+1)); 
        % Guardamos h y el error absoluto en la diagonal
        hs = [hs, h];
        errores = [errores, abs(R(n+1,n+1) - I_exacto)];
        % Criterio de convergencia
        if abs(R(n+1,n) - R(n+1,n+1)) < eps
            I_romberg = R(n+1,n+1);
            return;
        end
        n = n + 1; 
    end
end
function print_row(row)
    fprintf('%11.8f ', row);
    fprintf('\n');
end
