% Rango de tamaños de matriz
n_values = 2:14;
errors_LU = zeros(length(n_values), 1);
errors_Chol = zeros(length(n_values), 1);

% Calcular el error para cada tamaño de matriz
for k = 1:length(n_values)
    n = n_values(k);
    % Solución exacta (x_exact)
    x_exact = zeros(n, 1);
    x_exact(end) = 1;
    
    % Construir la matriz de Hilbert H_n
    H = zeros(n);
    for c = 1:n
        for r = 1:n
            H(r,c) = 1/(r+c-1);
        end
    end
    
    % Construir el vector b
    b = 1 ./ (n + (1:n) - 1)';  % b(i) = 1 / (n + i - 1)
    
    % Solución usando LU
    [L, U] = lu(H);
    y_LU = L \ b;
    x_LU = U \ y_LU;

    
    % Solución usando Cholesky
    L_chol = chol(H, 'lower');
    y_Chol = L_chol \ b;
    x_Chol = L_chol' \ y_Chol;
    
    % Calcular el error para LU
    errors_LU(k) = norm(x_LU - x_exact(1:n));

    % Calcular el error para Cholesky
    errors_Chol(k) =norm( x_Chol - x_exact(1:n));
 % Mostrar los errores en la tabla
    fprintf('%d\t\t%.5e\t%.5e\n', n, errors_LU(k), errors_Chol(k));
end

% Reemplazar ceros con un valor pequeño
errors_LU(errors_LU == 0) = 1e-16;
errors_Chol(errors_Chol == 0) = 1e-16;

% Graficar los errores con escala logarítmica
figure;
semilogy(n_values, errors_LU, 'b-o', 'LineWidth', 2, 'MarkerSize', 6);
hold on;
semilogy(n_values, errors_Chol, 'r-s', 'LineWidth', 2, 'MarkerSize', 6);
hold off;

% Etiquetas y título
xlabel('n (tamaño de la matriz)', 'FontSize', 13);
ylabel('Error ||x_{approx} - x_{exact}||', 'FontSize', 13);
title('Errores de la solución para diferentes tamaños n', 'FontSize', 14);
legend('LU', 'Cholesky', 'Location', 'Best');
grid on;



