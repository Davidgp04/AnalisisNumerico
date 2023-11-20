%SOR: Calcula la solución del sistema
%Ax=b con base en una condición inicial x0,mediante el método Gauss Seidel (relajado), depende del valor de w 
%entre (0,2)

function [E,s, x_values, message, radioEspectral] = SORrel(x0,A,b,Tol,niter,w)
    c=0;
    error=Tol+1;
    D=diag(diag(A));
    L=-tril(A,-1);
    U=-triu(A,+1);
    x_values = [];
    while error>Tol && c<niter

        T=inv(D-w*L)*((1-w)*D+w*U);
        C=w*inv(D-w*L)*b;
        x1=T*x0+C;
        E(c+1)=norm(abs((x1-x0)./x1),'inf');
        error=E(c+1);
        x_values = [x_values x1];
        x0=x1;
        c=c+1;
    end
    if error < Tol
        s=x0;
        n=c;
        s
        radioEspectral = max(abs(eig(T)))
        message = sprintf('Es una aproximacióon de la solucion del sistmea con una tolerancia= %f',Tol)
    else 
        s=x0;
        n=c;
        radioEspectral = max(abs(eig(T)))
        message = sprintf('Fracaso en %f iteraciones',niter) 
    end
end