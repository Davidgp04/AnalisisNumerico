%MatJacobiSeid: Calcula la solución del sistema
%Ax=b con base en una condición inicial x0,mediante el método de Jacobi o
%de Gauss Seidel (Matricial), depende del método elegido, se elige 0 o 1 en met
%respectivamente

function [E, s, x_values, message, radioEspectral] = MatJacobiSeid(x0,A,b,Tol,niter,met)
    c=0;
    error=Tol+1;
    D=diag(diag(A));
    L=-tril(A,-1);
    U=-triu(A,+1);

    x_values = [];

    while error>Tol && c<niter
        if met==0
            T=inv(D)*(L+U);
            C=inv(D)*b;
            x1=T*x0+C;
        end
        if met==1
            T=inv(D-L)*(U);
            C=inv(D-L)*b;
            x1=T*x0+C;
        end
        E(c+1)=norm(x1-x0,'inf');
        error=E(c+1);
        x_values = [x_values x1];
        x0=x1
        c=c+1;
    end
    if error < Tol
        s=x0;
        n=c;
        s
        radioEspectral = max(abs(eig(T)))
        message = sprintf('Es una aproximacion de la solución del sistema con una tolerancia = %f\n', Tol)
    else 
        s=x0;
        n=c;
        radioEspectral = max(abs(eig(T)))
        message = sprintf('Fracaso en %f iteraciones', niter) 
    end
    % Always return two values even if one is None
    if exist('E', 'var')
        s = s;
    else
        E = [];
    end
end