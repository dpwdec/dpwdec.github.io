---
layout: page
title: 📂
---
<style>
    ul {
        list-style: none;
        padding: 0;
        margin-bottom: 2px;
        margin-top: 0px;
    }

    label {
        cursor: pointer;
        border-bottom: none;
        font-weight: 450
    }

    input[type="checkbox"] {
        position: absolute;
        left: -9999px;
    }

    input[type="checkbox"]~ul {
        height: 0;
        transform: scaleY(0);
    }

    input[type="checkbox"]:checked~ul {
        height: 100%;
        transform-origin: top;
        transition: transform .2s ease-out;
        transform: scaleY(1);
    }

    /* turns the check into a closed folder by target labels AFTER an input */
    input+label:before {
        content: "📁";
        margin-right: 10px;
    }

    .file_content:before {
        content: "📄";
        margin-right: 10px;
    }

    /* toggles to open folder on label when checked */
    input[type="checkbox"]:checked~label:before {
        content: "📂";
        margin-right: 10px;
    }
</style>
<ul>
    <div name="contents-index">

        <l>
            <input type="checkbox" id="RxjtQrVRtR" checked>
            <label for="RxjtQrVRtR">Math</label>
            <ul>
                <l>
                    <input type="checkbox" id="RCzXrpChhZ">
                    <label for="RCzXrpChhZ">Exponentials</label>
                    <ul>
                        <l class="file_content"><a href='/math/exponentials/e'>E</a></l><br>
                        <l class="file_content"><a href='/math/exponentials/exponentials_in_other_bases'>Exponents in bases other than e</a></l><br>
                        <l class="file_content"><a href='/math/exponentials/exponents'>Exponents</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="TEGnJYLYHS">
                    <label for="TEGnJYLYHS">Linear Algebra</label>
                    <ul>
                        <l class="file_content"><a href='/math/linear_algebra/gaussian_elimination'>Gaussian Elimination</a></l><br>
                        <l class="file_content"><a href='/math/linear_algebra/homogenous_particular_matrices'>Homogenous and Particular Matrix Components</a></l><br>
                        <l class="file_content"><a href='/math/linear_algebra/linear_algebra'>Linear Algebra</a></l><br>
                        <l class="file_content"><a href='/math/linear_algebra/matrices'>Matrices</a></l><br>
                        <l class="file_content"><a href='/math/linear_algebra/point_slope'>Point Slope Formula</a></l><br>
                        <l class="file_content"><a href='/math/linear_algebra/simultaneous_equations'>Simultaneous Equations</a></l><br>
                        <l class="file_content"><a href='/math/linear_algebra/standard_form'>Standard Form</a></l><br>
                        <l class="file_content"><a href='/math/linear_algebra/tangent_lines'>Tangent Lines</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="CBiNaNuPvA">
                    <label for="CBiNaNuPvA">Logarithms</label>
                    <ul>
                        <l class="file_content"><a href='/math/logarithms/base_switch'>Base Switch</a></l><br>
                        <l class="file_content"><a href='/math/logarithms/change_of_base'>Change of Base</a></l><br>
                        <l class="file_content"><a href='/math/logarithms/logarithms'>Logarithms</a></l><br>
                        <l class="file_content"><a href='/math/logarithms/natural_logarithm'>Natural Logarithm</a></l><br>
                        <l class="file_content"><a href='/math/logarithms/power_rule'>Power Rule</a></l><br>
                        <l class="file_content"><a href='/math/logarithms/product_rule'>Product Rule</a></l><br>
                        <l class="file_content"><a href='/math/logarithms/quotient_rule'>Quotient Rule</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="fSJiQBdlgF">
                    <label for="fSJiQBdlgF">Sequences</label>
                    <ul>
                        <l class="file_content"><a href='/math/sequences/sigma_notation'>Sigma Notation</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="tZXdcJIRwN">
                    <label for="tZXdcJIRwN">Single Variable Calculus</label>
                    <ul>
                        <l class="file_content"><a href='/math/single_variable_calculus/chain_rule'>Chain Rule</a></l><br>
                        <l class="file_content"><a href='/math/single_variable_calculus/higher_derivatives'>Higher Derivatives</a></l><br>
                        <l class="file_content"><a href='/math/single_variable_calculus/implicit_derivatives'>Implicit Derivatives</a></l><br>
                        <l class="file_content"><a href='/math/single_variable_calculus/inverse_functions'>Inverse Functions</a></l><br>
                        <l class="file_content"><a href='/math/single_variable_calculus/product_rule'>Product Rule</a></l><br>
                        <l class="file_content"><a href='/math/single_variable_calculus/quotient_rule'>QuotienProduct Rule</a></l><br>
                        <l class="file_content"><a href='/math/single_variable_calculus/rational_exponents'>Rational Exponents</a></l><br>
                        <l class="file_content"><a href='/math/single_variable_calculus/reciprocals'>Reciprocals</a></l><br>
                        <l class="file_content"><a href='/math/single_variable_calculus/trig_function_derivatives'>Trigonometric Function Derivatives</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="RNDFmybmvi">
                    <label for="RNDFmybmvi">Trigonometry</label>
                    <ul>
                        <l class="file_content"><a href='/math/trigonometry/sum_and_difference_formulas'>Trigonometric Sum and Difference Formulas</a></l><br>
                    </ul>
                </l>
                <l class="file_content"><a href='/math/derivatives'>Derivatives</a></l><br>
                <l class="file_content"><a href='/math/limits'>Limits</a></l><br>
                <l class="file_content"><a href='/math/sets'>Sets</a></l><br>
            </ul>
        </l>

        <l>
            <input type="checkbox" id="hHWIqiegGd" checked>
            <label for="hHWIqiegGd">Programming</label>
            <ul>
                <l>
                    <input type="checkbox" id="YOIWpXzfgs">
                    <label for="YOIWpXzfgs">Ansible</label>
                    <ul>
                        <l class="file_content"><a href='/programming/ansible/ansible'>Ansible</a></l><br>
                        <l class="file_content"><a href='/programming/ansible/async'>Async</a></l><br>
                        <l class="file_content"><a href='/programming/ansible/failure'>Failure</a></l><br>
                        <l class="file_content"><a href='/programming/ansible/loops'>Loops</a></l><br>
                        <l class="file_content"><a href='/programming/ansible/when'>When</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="lvdtUSksuq">
                    <label for="lvdtUSksuq">Architecture</label>
                    <ul>
                        <l class="file_content"><a href='/programming/architecture/concerns'>Concerns</a></l><br>
                        <l class="file_content"><a href='/programming/architecture/oop'>OOP</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="xTAKywpfcu">
                    <label for="xTAKywpfcu">Computer Graphics</label>
                    <ul>
                        <l class="file_content"><a href='/programming/computer_graphics/image_blending'>Image Blending</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="HmTRaJuGgq">
                    <label for="HmTRaJuGgq">Databases</label>
                    <ul>
                        <l class="file_content"><a href='/programming/databases/db'>Databases</a></l><br>
                        <l class="file_content"><a href='/programming/databases/migrations'>Migrations</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="lKZBZhwERJ">
                    <label for="lKZBZhwERJ">Devops</label>
                    <ul>
                        <l>
                            <input type="checkbox" id="zQgrnuHuOf">
                            <label for="zQgrnuHuOf">Cloud Providers</label>
                            <ul>
                                <l>
                                    <input type="checkbox" id="PnNnAfFkTw">
                                    <label for="PnNnAfFkTw">AWS</label>
                                    <ul>
                                        <l>
                                            <input type="checkbox" id="rFQEWXeGyh">
                                            <label for="rFQEWXeGyh">Cli</label>
                                            <ul>
                                                <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/cli/configure'>Configure</a></l><br>
                                                <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/cli/sts'>STS</a></l><br>
                                            </ul>
                                        </l>

                                        <l>
                                            <input type="checkbox" id="dyKcexvuNH">
                                            <label for="dyKcexvuNH">Dotnet</label>
                                            <ul>
                                                <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/dotnet/credentials'>Credentials</a></l><br>
                                                <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/dotnet/sns'>SNS</a></l><br>
                                                <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/dotnet/sqs'>SQS</a></l><br>
                                            </ul>
                                        </l>

                                        <l>
                                            <input type="checkbox" id="BYkhDolDRm">
                                            <label for="BYkhDolDRm">Ec 2</label>
                                            <ul>
                                                <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/ec_2/alb'>Application Load Balancers</a></l><br>
                                                <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/ec_2/asg'>Auto Scaling Groups</a></l><br>
                                                <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/ec_2/ec2'>EC2</a></l><br>
                                                <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/ec_2/vpc'>Virtual Private Cloud</a></l><br>
                                            </ul>
                                        </l>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/acl'>ACL</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/aws'>aws</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/cli'>CLI</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/cloudfront'>Cloudfront</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/cross_account_sns_to_sqs'>Cross Account SNS to SQS</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/iam'>IAM</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/lambda'>Lambda</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/route_53'>Route 53</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/s3'>S3</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/sdk'>SDK</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/secrets_manager'>Secrets Manager</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/sns'>Simple Notification Service</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/sqs'>Simple Queue Service</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/cloud_providers/a_w_s/waf'>WAF</a></l><br>
                                    </ul>
                                </l>
                                <l class="file_content"><a href='/programming/devops/cloud_providers/cloud_computing'>Cloud Computing</a></l><br>
                            </ul>
                        </l>

                        <l>
                            <input type="checkbox" id="bgRqbsEHZI">
                            <label for="bgRqbsEHZI">Events</label>
                            <ul>
                                <l class="file_content"><a href='/programming/devops/events/async_api'>Async APIs</a></l><br>
                            </ul>
                        </l>

                        <l>
                            <input type="checkbox" id="FDOIksmtuo">
                            <label for="FDOIksmtuo">Localstack</label>
                            <ul>
                                <l class="file_content"><a href='/programming/devops/localstack/aws_cli'>AWS CLI</a></l><br>
                            </ul>
                        </l>

                        <l>
                            <input type="checkbox" id="lmkbPmuvUS">
                            <label for="lmkbPmuvUS">Pulumi</label>
                            <ul>
                                <l>
                                    <input type="checkbox" id="czGaMhivob">
                                    <label for="czGaMhivob">Dotnet</label>
                                    <ul>
                                        <l class="file_content"><a href='/programming/devops/pulumi/dotnet/dependency_injection'>Running</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/pulumi/dotnet/explicit_dependencies'>Explicit Dependencies</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/pulumi/dotnet/inputs_and_outputs'>Inputs and Outputs</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/pulumi/dotnet/running'>Running</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/pulumi/dotnet/unit_testing'>Unit Testing</a></l><br>
                                    </ul>
                                </l>
                                <l class="file_content"><a href='/programming/devops/pulumi/secrets'>Secrets</a></l><br>
                                <l class="file_content"><a href='/programming/devops/pulumi/setup'>Set Up</a></l><br>
                                <l class="file_content"><a href='/programming/devops/pulumi/stack'>Stack</a></l><br>
                            </ul>
                        </l>

                        <l>
                            <input type="checkbox" id="eDoesSuVyw">
                            <label for="eDoesSuVyw">Serverless Framework</label>
                            <ul>
                                <l class="file_content"><a href='/programming/devops/serverless_framework/functions'>Functions</a></l><br>
                                <l class="file_content"><a href='/programming/devops/serverless_framework/middleware'>Middleware</a></l><br>
                                <l class="file_content"><a href='/programming/devops/serverless_framework/params'>Params</a></l><br>
                                <l class="file_content"><a href='/programming/devops/serverless_framework/providers'>Providers</a></l><br>
                                <l class="file_content"><a href='/programming/devops/serverless_framework/resources'>Resources</a></l><br>
                                <l class="file_content"><a href='/programming/devops/serverless_framework/serverless'>Serverless</a></l><br>
                            </ul>
                        </l>

                        <l>
                            <input type="checkbox" id="hETmKHaFUG">
                            <label for="hETmKHaFUG">Terraform</label>
                            <ul>
                                <l>
                                    <input type="checkbox" id="FJhiZhldiD">
                                    <label for="FJhiZhldiD">Functions</label>
                                    <ul>
                                        <l class="file_content"><a href='/programming/devops/terraform/functions/try'>Try</a></l><br>
                                    </ul>
                                </l>

                                <l>
                                    <input type="checkbox" id="zPwwCKnajK">
                                    <label for="zPwwCKnajK">Meta Arguments</label>
                                    <ul>
                                        <l class="file_content"><a href='/programming/devops/terraform/meta_arguments/count'>Count</a></l><br>
                                        <l class="file_content"><a href='/programming/devops/terraform/meta_arguments/for_each'>For Each</a></l><br>
                                    </ul>
                                </l>
                                <l class="file_content"><a href='/programming/devops/terraform/commands'>Commands</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/data'>Data</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/locals'>Locals</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/modules'>Modules</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/output'>Output</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/path'>Path</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/project_structure'>Project Structure</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/providers'>Providers</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/references'>References</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/resources'>Resources</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/terraform'>Terraform</a></l><br>
                                <l class="file_content"><a href='/programming/devops/terraform/variables'>Variables</a></l><br>
                            </ul>
                        </l>
                        <l class="file_content"><a href='/programming/devops/containerisation'>Containerisation</a></l><br>
                        <l class="file_content"><a href='/programming/devops/curl'>Curl</a></l><br>
                        <l class="file_content"><a href='/programming/devops/kong'>Kong</a></l><br>
                        <l class="file_content"><a href='/programming/devops/microservices'>Microservices</a></l><br>
                        <l class="file_content"><a href='/programming/devops/open_api_spec'>OpenAPISpec</a></l><br>
                        <l class="file_content"><a href='/programming/devops/proxy'>Proxy</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="mEMsskVxoN">
                    <label for="mEMsskVxoN">Docker</label>
                    <ul>
                        <l class="file_content"><a href='/programming/docker/bind_mounts'>Bind Mounts</a></l><br>
                        <l class="file_content"><a href='/programming/docker/docker'>Docker</a></l><br>
                        <l class="file_content"><a href='/programming/docker/docker_compose'>Docker Compose</a></l><br>
                        <l class="file_content"><a href='/programming/docker/docker_file'>Dockerfile</a></l><br>
                        <l class="file_content"><a href='/programming/docker/images'>Images</a></l><br>
                        <l class="file_content"><a href='/programming/docker/volumes'>Volumes</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="HcRNxbduLK">
                    <label for="HcRNxbduLK">Dotnet</label>
                    <ul>
                        <l>
                            <input type="checkbox" id="HgEQwlNxvf">
                            <label for="HgEQwlNxvf">Cli</label>
                            <ul>
                                <l class="file_content"><a href='/programming/dotnet/cli/project'>Project</a></l><br>
                                <l class="file_content"><a href='/programming/dotnet/cli/publish'>Publish</a></l><br>
                                <l class="file_content"><a href='/programming/dotnet/cli/solution'>Solution</a></l><br>
                                <l class="file_content"><a href='/programming/dotnet/cli/test'>Test</a></l><br>
                            </ul>
                        </l>
                        <l class="file_content"><a href='/programming/dotnet/Asp'>ASP</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Async'>Async</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Attributes'>Attributes</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Automapper'>Automapper</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Binary'>Binary</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Collections'>Collections</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/CommandLineUtils'>Command Line Utils</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/DataAnnotations'>Data Annotations</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/DependencyInjection'>Dependency Injection</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Dotnet'>.NET</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Dynamic'>Dynamic</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/EntityFramework'>Entity Framework</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/ExtensionMethods'>Extension Methods</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Functions'>Functions</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Guid'>Guid</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Handlebars'>Handlebars</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Ienum'>IEnumerable and IEnumerator</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Json'>JSON</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Loops'>Loops</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Moq'>Moq</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Nuget'>Nuget</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Nunit'>NUnit</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Rm'>Resource Management</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Types'>Types</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/Xunit'>XUnit</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/classes'>Classes</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/command_line_parser'>Command Line Parser</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/conditionals'>Conditionals</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/embedded_resources'>Embedded Resources</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/enums'>Enums</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/file_system'>File System</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/fluent_assertions'>Fluent Assertions</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/logging'>Logging</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/project'>Project</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/reflection'>Reflection</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/service_provider'>Service Prodiver</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/start_up'>Start Up</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/static_properties'>Static Properties</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/strings'>Strings</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/switch'>Switch</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/xeger'>Xeger</a></l><br>
                        <l class="file_content"><a href='/programming/dotnet/yamldotnet'>YamlDotNet</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="OoXOSOBlqX">
                    <label for="OoXOSOBlqX">Functional Programming</label>
                    <ul>
                        <l class="file_content"><a href='/programming/functional_programming/func_prog'>Functional Programming</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="eKXBCsrCTN">
                    <label for="eKXBCsrCTN">Git</label>
                    <ul>
                        <l>
                            <input type="checkbox" id="jyfzSbKAPz">
                            <label for="jyfzSbKAPz">Github</label>
                            <ul>
                                <l class="file_content"><a href='/programming/git/github/actions'>Github Actions</a></l><br>
                                <l class="file_content"><a href='/programming/git/github/searching'>Searching</a></l><br>
                            </ul>
                        </l>
                        <l class="file_content"><a href='/programming/git/diff'>diff</a></l><br>
                        <l class="file_content"><a href='/programming/git/git'>Git</a></l><br>
                        <l class="file_content"><a href='/programming/git/log'>log</a></l><br>
                        <l class="file_content"><a href='/programming/git/rebase'>Rebase</a></l><br>
                        <l class="file_content"><a href='/programming/git/whatchanged'>whatchanged</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="QoctnmFWKg">
                    <label for="QoctnmFWKg">Go</label>
                    <ul>
                        <l class="file_content"><a href='/programming/go/enum'>enum</a></l><br>
                        <l class="file_content"><a href='/programming/go/fmt'>fmt</a></l><br>
                        <l class="file_content"><a href='/programming/go/functions'>functions</a></l><br>
                        <l class="file_content"><a href='/programming/go/import'>import</a></l><br>
                        <l class="file_content"><a href='/programming/go/package'>package</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="uNiYOBpmod">
                    <label for="uNiYOBpmod">Haskell</label>
                    <ul>
                        <l class="file_content"><a href='/programming/haskell/guards'>Guards</a></l><br>
                        <l class="file_content"><a href='/programming/haskell/haskell'>Haskell</a></l><br>
                        <l class="file_content"><a href='/programming/haskell/higher_order_functions'>Higher Order Functions</a></l><br>
                        <l class="file_content"><a href='/programming/haskell/lists'>Lists</a></l><br>
                        <l class="file_content"><a href='/programming/haskell/operators'>Operators</a></l><br>
                        <l class="file_content"><a href='/programming/haskell/patterns'>Pattern Matching</a></l><br>
                        <l class="file_content"><a href='/programming/haskell/recursion'>Recursion</a></l><br>
                        <l class="file_content"><a href='/programming/haskell/types'>Types</a></l><br>
                        <l class="file_content"><a href='/programming/haskell/where'>Where</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="BoAQzgJLxP">
                    <label for="BoAQzgJLxP">Js</label>
                    <ul>
                        <l>
                            <input type="checkbox" id="lsIosXhzBH">
                            <label for="lsIosXhzBH">Node</label>
                            <ul>
                                <l class="file_content"><a href='/programming/js/Node/assert'>Assert</a></l><br>
                                <l class="file_content"><a href='/programming/js/Node/child_process'>Child Process</a></l><br>
                                <l class="file_content"><a href='/programming/js/Node/node'>Node</a></l><br>
                                <l class="file_content"><a href='/programming/js/Node/query_string'>querstring</a></l><br>
                            </ul>
                        </l>

                        <l>
                            <input type="checkbox" id="VMXsZczYoP">
                            <label for="VMXsZczYoP">D3</label>
                            <ul>
                                <l class="file_content"><a href='/programming/js/d3/color'>Color</a></l><br>
                                <l class="file_content"><a href='/programming/js/d3/svg'>SVG</a></l><br>
                                <l class="file_content"><a href='/programming/js/d3/transitions'>Transitions</a></l><br>
                            </ul>
                        </l>

                        <l>
                            <input type="checkbox" id="vPixKGZrNc">
                            <label for="vPixKGZrNc">Mocha</label>
                            <ul>
                                <l class="file_content"><a href='/programming/js/mocha/code_runner'>Code Runner</a></l><br>
                                <l class="file_content"><a href='/programming/js/mocha/mocha'>Mocha</a></l><br>
                            </ul>
                        </l>

                        <l>
                            <input type="checkbox" id="GEsVCETwbS">
                            <label for="GEsVCETwbS">P5js</label>
                            <ul>
                                <l class="file_content"><a href='/programming/js/p5js/dom_elements'>DOM Elements</a></l><br>
                                <l class="file_content"><a href='/programming/js/p5js/embedding'>Embedding</a></l><br>
                                <l class="file_content"><a href='/programming/js/p5js/p5js'>p5.js</a></l><br>
                            </ul>
                        </l>

                        <l>
                            <input type="checkbox" id="bijsnIHEoI">
                            <label for="bijsnIHEoI">Typescript</label>
                            <ul>
                                <l>
                                    <input type="checkbox" id="yGWOEqQfTk">
                                    <label for="yGWOEqQfTk">Testing</label>
                                    <ul>
                                        <l class="file_content"><a href='/programming/js/typescript/testing/jest'>Jest</a></l><br>
                                    </ul>
                                </l>
                                <l class="file_content"><a href='/programming/js/typescript/destructuring'>Destructuring</a></l><br>
                                <l class="file_content"><a href='/programming/js/typescript/functions'>Functions</a></l><br>
                                <l class="file_content"><a href='/programming/js/typescript/indexable_types'>Indexable Types</a></l><br>
                                <l class="file_content"><a href='/programming/js/typescript/narrowing'>Narrowing</a></l><br>
                                <l class="file_content"><a href='/programming/js/typescript/types'>Types</a></l><br>
                                <l class="file_content"><a href='/programming/js/typescript/typescript'>Typescript</a></l><br>
                            </ul>
                        </l>
                        <l class="file_content"><a href='/programming/js/ajax'>Ajax</a></l><br>
                        <l class="file_content"><a href='/programming/js/array'>Array</a></l><br>
                        <l class="file_content"><a href='/programming/js/cypress'>Cypress</a></l><br>
                        <l class="file_content"><a href='/programming/js/dot_env'>Dotenv</a></l><br>
                        <l class="file_content"><a href='/programming/js/express'>Express</a></l><br>
                        <l class="file_content"><a href='/programming/js/find'>Find</a></l><br>
                        <l class="file_content"><a href='/programming/js/handlebars'>Handlebars</a></l><br>
                        <l class="file_content"><a href='/programming/js/jasmine'>Jasmine</a></l><br>
                        <l class="file_content"><a href='/programming/js/javascript'>JavaScript</a></l><br>
                        <l class="file_content"><a href='/programming/js/javascript_objects'>JavaScript Objects</a></l><br>
                        <l class="file_content"><a href='/programming/js/jest'>Jest</a></l><br>
                        <l class="file_content"><a href='/programming/js/jquery'>jQuery</a></l><br>
                        <l class="file_content"><a href='/programming/js/jsdelivr'>jsdelivr</a></l><br>
                        <l class="file_content"><a href='/programming/js/jsdom'>Javascript DOM</a></l><br>
                        <l class="file_content"><a href='/programming/js/jsonata'>Jsonata</a></l><br>
                        <l class="file_content"><a href='/programming/js/mongo_db'>MongoDB</a></l><br>
                        <l class="file_content"><a href='/programming/js/prototype'>Prototype</a></l><br>
                        <l class="file_content"><a href='/programming/js/strings'>Strings</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="toyUaOqfNT">
                    <label for="toyUaOqfNT">Kafka</label>
                    <ul>
                        <l class="file_content"><a href='/programming/kafka/kafka'>Kafka</a></l><br>
                        <l class="file_content"><a href='/programming/kafka/topics'>Topics</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="GSKxKDNZrh">
                    <label for="GSKxKDNZrh">Kubernetes</label>
                    <ul>
                        <l class="file_content"><a href='/programming/kubernetes/architecture'>Architecture</a></l><br>
                        <l class="file_content"><a href='/programming/kubernetes/kubectl'>Kubectl</a></l><br>
                        <l class="file_content"><a href='/programming/kubernetes/kubernetes'>Kubernetes</a></l><br>
                        <l class="file_content"><a href='/programming/kubernetes/minikube'>Minikube</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="ChLwZXLAUu">
                    <label for="ChLwZXLAUu">Language</label>
                    <ul>
                        <l class="file_content"><a href='/programming/language/japanese_keyboard'>Japanese Keyboard</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="zvIVDUgjeZ">
                    <label for="zvIVDUgjeZ">Linux</label>
                    <ul>
                        <l>
                            <input type="checkbox" id="BTqbmMVIAO">
                            <label for="BTqbmMVIAO">Bash</label>
                            <ul>
                                <l class="file_content"><a href='/programming/linux/bash/bash'>Bash</a></l><br>
                                <l class="file_content"><a href='/programming/linux/bash/conditionals'>Conditionals</a></l><br>
                            </ul>
                        </l>
                        <l class="file_content"><a href='/programming/linux/apt'>Apt</a></l><br>
                        <l class="file_content"><a href='/programming/linux/cli'>CLI</a></l><br>
                        <l class="file_content"><a href='/programming/linux/cut'>Cut</a></l><br>
                        <l class="file_content"><a href='/programming/linux/file_descriptors'>File Descriptors</a></l><br>
                        <l class="file_content"><a href='/programming/linux/imagemagick'>Imagemagick</a></l><br>
                        <l class="file_content"><a href='/programming/linux/jq'>JQ</a></l><br>
                        <l class="file_content"><a href='/programming/linux/linux'>Linux </a></l><br>
                        <l class="file_content"><a href='/programming/linux/mkdir'>Mkdir</a></l><br>
                        <l class="file_content"><a href='/programming/linux/ps'>Ps</a></l><br>
                        <l class="file_content"><a href='/programming/linux/shift'>Shift</a></l><br>
                        <l class="file_content"><a href='/programming/linux/tee'>Tee</a></l><br>
                        <l class="file_content"><a href='/programming/linux/tty'>TTY</a></l><br>
                        <l class="file_content"><a href='/programming/linux/zip'>Zip</a></l><br>
                        <l class="file_content"><a href='/programming/linux/zsh'>Zsh</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="nJikJBfkYE">
                    <label for="nJikJBfkYE">Oauth</label>
                    <ul>
                        <l class="file_content"><a href='/programming/oauth/jwt'>JWT</a></l><br>
                        <l class="file_content"><a href='/programming/oauth/oauth'>OAuth</a></l><br>
                        <l class="file_content"><a href='/programming/oauth/oidc'>OIDC</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="gGITnsNwKj">
                    <label for="gGITnsNwKj">Python</label>
                    <ul>
                        <l>
                            <input type="checkbox" id="lculDdpAOW">
                            <label for="lculDdpAOW">Data Classes</label>
                            <ul>
                                <l class="file_content"><a href='/programming/python/data_classes/named_tuples'>Named Tuples</a></l><br>
                                <l class="file_content"><a href='/programming/python/data_classes/record_class'>Record Class</a></l><br>
                            </ul>
                        </l>

                        <l>
                            <input type="checkbox" id="aXxnsmdBpj">
                            <label for="aXxnsmdBpj">Libraries</label>
                            <ul>
                                <l class="file_content"><a href='/programming/python/libraries/gspread'>gspread</a></l><br>
                            </ul>
                        </l>
                        <l class="file_content"><a href='/programming/python/argparse'>argparse</a></l><br>
                        <l class="file_content"><a href='/programming/python/boto3'>Boto 3</a></l><br>
                        <l class="file_content"><a href='/programming/python/command_line_arguments'>Command Line Arguments</a></l><br>
                        <l class="file_content"><a href='/programming/python/files'>Files</a></l><br>
                        <l class="file_content"><a href='/programming/python/http_server'>HTTP Server</a></l><br>
                        <l class="file_content"><a href='/programming/python/injector'>Injector</a></l><br>
                        <l class="file_content"><a href='/programming/python/json'>json</a></l><br>
                        <l class="file_content"><a href='/programming/python/list_comprehensions'>List Comprehensions</a></l><br>
                        <l class="file_content"><a href='/programming/python/lists'>Lists</a></l><br>
                        <l class="file_content"><a href='/programming/python/print'>Print</a></l><br>
                        <l class="file_content"><a href='/programming/python/py_test'>Pytest</a></l><br>
                        <l class="file_content"><a href='/programming/python/python'>Python</a></l><br>
                        <l class="file_content"><a href='/programming/python/repl'>REPL</a></l><br>
                        <l class="file_content"><a href='/programming/python/strings'>Strings</a></l><br>
                        <l class="file_content"><a href='/programming/python/sub_process'>subprocess</a></l><br>
                        <l class="file_content"><a href='/programming/python/type_hints'>Type Hints</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="WTkIYikdxa">
                    <label for="WTkIYikdxa">React</label>
                    <ul>
                        <l class="file_content"><a href='/programming/react/generator-templates'>Generator Templates</a></l><br>
                        <l class="file_content"><a href='/programming/react/react'>React</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="IneboisQLL">
                    <label for="IneboisQLL">Regular Expressions</label>
                    <ul>
                        <l class="file_content"><a href='/programming/regular_expressions/mode_modifiers'>Mode Modifiers</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="GQdZmdUvdN">
                    <label for="GQdZmdUvdN">Rust</label>
                    <ul>
                        <l>
                            <input type="checkbox" id="wcsitWarTJ">
                            <label for="wcsitWarTJ">Serde</label>
                            <ul>
                                <l class="file_content"><a href='/programming/rust/serde/defaults'>Defaults</a></l><br>
                                <l class="file_content"><a href='/programming/rust/serde/renaming'>Renaming</a></l><br>
                                <l class="file_content"><a href='/programming/rust/serde/serde'>Serde</a></l><br>
                            </ul>
                        </l>
                        <l class="file_content"><a href='/programming/rust/bool'>Bool</a></l><br>
                        <l class="file_content"><a href='/programming/rust/cargo'>Cargo</a></l><br>
                        <l class="file_content"><a href='/programming/rust/collections'>Collections</a></l><br>
                        <l class="file_content"><a href='/programming/rust/concurrency'>Concurrency</a></l><br>
                        <l class="file_content"><a href='/programming/rust/enums'>Enums</a></l><br>
                        <l class="file_content"><a href='/programming/rust/extern_crates'>Extern Crates</a></l><br>
                        <l class="file_content"><a href='/programming/rust/files'>Files</a></l><br>
                        <l class="file_content"><a href='/programming/rust/functions'>Functions</a></l><br>
                        <l class="file_content"><a href='/programming/rust/handlebars'>Handlebars</a></l><br>
                        <l class="file_content"><a href='/programming/rust/hashmap'>Hash Map</a></l><br>
                        <l class="file_content"><a href='/programming/rust/iterators'>Iterators</a></l><br>
                        <l class="file_content"><a href='/programming/rust/itertools'>Itertools</a></l><br>
                        <l class="file_content"><a href='/programming/rust/lifetimes'>Lifetimes</a></l><br>
                        <l class="file_content"><a href='/programming/rust/mutability'>Mutability</a></l><br>
                        <l class="file_content"><a href='/programming/rust/num'>Num</a></l><br>
                        <l class="file_content"><a href='/programming/rust/operators'>Operators</a></l><br>
                        <l class="file_content"><a href='/programming/rust/rust'>Rust</a></l><br>
                        <l class="file_content"><a href='/programming/rust/strings'>Strings</a></l><br>
                        <l class="file_content"><a href='/programming/rust/structs'>Structs</a></l><br>
                        <l class="file_content"><a href='/programming/rust/strum'>Strum</a></l><br>
                        <l class="file_content"><a href='/programming/rust/types'>Types</a></l><br>
                        <l class="file_content"><a href='/programming/rust/vec'>Vec</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="RZZzwckBhx">
                    <label for="RZZzwckBhx">Shaders</label>
                    <ul>
                        <l>
                            <input type="checkbox" id="AniQZhoARC">
                            <label for="AniQZhoARC">Glsl</label>
                            <ul>
                                <l class="file_content"><a href='/programming/shaders/glsl/webgl'>Web GL</a></l><br>
                            </ul>
                        </l>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="yDWdiYEjfB">
                    <label for="yDWdiYEjfB">Vim</label>
                    <ul>
                        <l class="file_content"><a href='/programming/vim/vim'>Vim</a></l><br>
                    </ul>
                </l>

                <l>
                    <input type="checkbox" id="oTwFDjeVSN">
                    <label for="oTwFDjeVSN">Web</label>
                    <ul>
                        <l class="file_content"><a href='/programming/web/cookies'>Cookies</a></l><br>
                        <l class="file_content"><a href='/programming/web/cors'>CORS</a></l><br>
                        <l class="file_content"><a href='/programming/web/dns'>DNS</a></l><br>
                        <l class="file_content"><a href='/programming/web/rest'>REST</a></l><br>
                        <l class="file_content"><a href='/programming/web/www'>Web Structures</a></l><br>
                    </ul>
                </l>
                <l class="file_content"><a href='/programming/actix'>Actix Web</a></l><br>
                <l class="file_content"><a href='/programming/artifactory'>Artifactory</a></l><br>
                <l class="file_content"><a href='/programming/atom'>atom</a></l><br>
                <l class="file_content"><a href='/programming/c'>C</a></l><br>
                <l class="file_content"><a href='/programming/capybara'>Sinatra</a></l><br>
                <l class="file_content"><a href='/programming/cmd_line'>Command Line</a></l><br>
                <l class="file_content"><a href='/programming/css'>CSS</a></l><br>
                <l class="file_content"><a href='/programming/data_mapper'>Datamapper</a></l><br>
                <l class="file_content"><a href='/programming/discord'>Discord</a></l><br>
                <l class="file_content"><a href='/programming/discord_js'>Discord.js</a></l><br>
                <l class="file_content"><a href='/programming/dmd'>dmd</a></l><br>
                <l class="file_content"><a href='/programming/flask'>Flask</a></l><br>
                <l class="file_content"><a href='/programming/gmail'>Gmail</a></l><br>
                <l class="file_content"><a href='/programming/handlebars'>Handlebars</a></l><br>
                <l class="file_content"><a href='/programming/heroku'>Heroku</a></l><br>
                <l class="file_content"><a href='/programming/html'>HTML</a></l><br>
                <l class="file_content"><a href='/programming/ieee_754'>IEEE754</a></l><br>
                <l class="file_content"><a href='/programming/jet_brains'>JetBrains</a></l><br>
                <l class="file_content"><a href='/programming/jinja'>Jinja</a></l><br>
                <l class="file_content"><a href='/programming/latex'>Latex</a></l><br>
                <l class="file_content"><a href='/programming/markdown'>Markdown</a></l><br>
                <l class="file_content"><a href='/programming/mathjax'>Mathjax</a></l><br>
                <l class="file_content"><a href='/programming/multer'>Multer</a></l><br>
                <l class="file_content"><a href='/programming/psql'>PostgreSQL</a></l><br>
                <l class="file_content"><a href='/programming/refactoring'>Refactoring</a></l><br>
                <l class="file_content"><a href='/programming/rider'>Rider</a></l><br>
                <l class="file_content"><a href='/programming/rk61'>rk61</a></l><br>
                <l class="file_content"><a href='/programming/rspec'>RSpec</a></l><br>
                <l class="file_content"><a href='/programming/ruby'>Ruby</a></l><br>
                <l class="file_content"><a href='/programming/sinatra'>Sinatra</a></l><br>
                <l class="file_content"><a href='/programming/sql'>SQL</a></l><br>
                <l class="file_content"><a href='/programming/sql_alchemy'>SQL Alchemy</a></l><br>
                <l class="file_content"><a href='/programming/travis'>Travis CI</a></l><br>
                <l class="file_content"><a href='/programming/unit_test'>Unittest</a></l><br>
                <l class="file_content"><a href='/programming/virtualenv'>Virtual Env</a></l><br>
                <l class="file_content"><a href='/programming/vs_code'>Vs Code</a></l><br>
                <l class="file_content"><a href='/programming/youtube_data'>Youtube Data</a></l><br>
            </ul>
        </l>

    </div>
</ul>