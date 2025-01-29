% Parámetro de tamaño

for n=1:15
    
    % Construir la matriz de Hilbert H_n
    H = zeros(n);
    for c = 1:n
        for r = 1:n
            H(r,c) = 1/(r+c-1);
        end
    end
    
    % Construir el vector b
    b = 1 ./ (n + (1:n) - 1)';  % b(i) = 1 / (n + i - 1)
    
    % Factorización LU
    [L, U] = lu(H);
    
    % Resolver el sistema utilizando LU (H * x = b)
    % Paso 1: Resolver L * y = b usando sustitución hacia adelante
    y = L \ b;
    
    % Paso 2: Resolver U * x = y usando sustitución hacia atrás
    x_LU = U \ y;
    
    % Factorización de Cholesky
    L_chol = chol(H, 'lower');
    
    % Resolver el sistema utilizando Cholesky (H * x = b)
    % Paso 1: Resolver L_chol * y = b usando sustitución hacia adelante
    y_chol = L_chol \ b;
    
    % Paso 2: Resolver L_chol' * x = y usando sustitución hacia atrás
    x_chol = L_chol' \ y_chol;
    
    % Mostrar los resultados
    disp('Solución usando LU:');
    disp(x_LU);
    
    disp('Solución usando Cholesky:');
    disp(x_chol);
    disp(cond(H));
end
